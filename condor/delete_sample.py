import os
import random

def get_total_size(file_list):
    """计算文件列表中所有文件的总大小"""
    return sum(os.path.getsize(file) for file in file_list)

def delete_random_files(file_list, target_size, current_size):
    """删除随机文件直到文件总大小接近目标大小"""
    while current_size > target_size and file_list:
        # 随机选择一个文件
        file_to_delete = random.choice(file_list)
        file_list.remove(file_to_delete)  # 从列表中移除该文件
        os.remove(file_to_delete)  # 删除文件
        current_size = get_total_size(file_list)  # 更新剩余文件的总大小
        print(f"Deleted: {file_to_delete}, Current total size: {current_size / (1024**3):.2f} GB")
    
    return file_list, current_size

def find_root_files(root_directory):
    """递归查找所有的 .root 文件"""
    root_files = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.root'):
                root_files.append(os.path.join(root, file))
    return root_files

def main():
    # 设置目标文件夹路径
    sample_list  = ["TTHHTo4b_HEFT_c2-6_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_c2-3_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_c2-m1_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kl-0p5_c2-1_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kl-2_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kl-3_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kt-2_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8"]
    for sample in sample_list:
        folder_path = "/eos/user/a/acarvalh/nanoAOD_HHH6B/2016/mc/%s"%(sample)
        
        # 设置目标大小（4 GB）
        target_size = 4 * 1024**3  # 4GB in bytes
        
        # 获取该目录下的所有 .root 文件
        root_files = find_root_files(folder_path)
        
        # 获取当前所有文件的总大小
        current_size = get_total_size(root_files)
        print(f"Initial total size: {current_size / (1024**3):.2f} GB")
        
        if current_size <= target_size:
            print("The total size is already less than or equal to the target size.")
            return
        
        # 删除随机文件直到大小符合要求
        remaining_files, final_size = delete_random_files(root_files, target_size, current_size)
        
        print(f"Final total size: {final_size / (1024**3):.2f} GB")
        print(f"Remaining {len(remaining_files)} files.")

if __name__ == "__main__":
    main()
