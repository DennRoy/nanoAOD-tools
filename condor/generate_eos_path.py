import os

def generate_list_file(root_dir, output_list_file):
    """
    递归搜索根目录下的所有子目录，找到所有的 .root 文件，并将完整路径写入 .list 文件。

    :param root_dir: 包含子目录和 .root 文件的根目录路径
    :param output_list_file: 输出的 .list 文件路径
    """
    try:
        with open(output_list_file, 'w') as f:
            for dirpath, _, filenames in os.walk(root_dir):
                for filename in filenames:
                    if filename.endswith(".root"):
                        full_path = os.path.join(dirpath, filename)
                        f.write(full_path + '\n')
        print(f"已成功生成 {output_list_file}")
    except Exception as e:
        print(f"生成列表文件时出错: {e}")
# 示例用法
sample_list  = ["TTHHTo4b_HEFT_c2-6_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_c2-3_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_c2-m1_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kl-0p5_c2-1_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kl-2_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kl-3_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_HEFT_kt-2_TuneCP5_13TeV-madgraph-pythia8","TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8"]
for sample in sample_list:

    root_directory = "/eos/user/a/acarvalh/nanoAOD_HHH6B/2017/mc/%s"%(sample)  
    # root_directory = "/eos/cms/store/group/phys_higgs/cmshhh/NanoAODv9PNetAK4/output_2017/%s"%(sample)  
    path_for_output = "/afs/cern.ch/user/x/xgeng/HHH/CMSSW_13_3_0/src/PhysicsTools/NanoAODTools/condor/list/nano/v9-pnetAK4/2017"
    output_file = "%s/%s.list"%(path_for_output,sample)  # 输出的 .list 文件名
    generate_list_file(root_directory, output_file)
