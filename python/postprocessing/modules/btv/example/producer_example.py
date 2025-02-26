class FlavTreeProducer(Module, object):

    def __init__(self, channel, **kwargs):

        # ParticleNetAK4 -- exclusive b- and c-tagging categories
        # 5x: b-tagged; 4x: c-tagged; 0: light
        if self._year in (2017, 2018):
            self.jetTagWPs = {
                54: '(pn_b_plus_c>0.5) & (pn_b_vs_c>0.99)',
                53: '(pn_b_plus_c>0.5) & (0.96<pn_b_vs_c<=0.99)',
                52: '(pn_b_plus_c>0.5) & (0.88<pn_b_vs_c<=0.96)',
                51: '(pn_b_plus_c>0.5) & (0.70<pn_b_vs_c<=0.88)',
                50: '(pn_b_plus_c>0.5) & (0.40<pn_b_vs_c<=0.70)',

                44: '(pn_b_plus_c>0.5) & (pn_b_vs_c<=0.05)',
                43: '(pn_b_plus_c>0.5) & (0.05<pn_b_vs_c<=0.15)',
                42: '(pn_b_plus_c>0.5) & (0.15<pn_b_vs_c<=0.40)',
                41: '(0.2<pn_b_plus_c<=0.5)',
                40: '(0.1<pn_b_plus_c<=0.2)',

                0: '(pn_b_plus_c<=0.1)',
            }
        elif self._year in (2015, 2016):
            self.jetTagWPs = {
                54: '(pn_b_plus_c>0.35) & (pn_b_vs_c>0.99)',
                53: '(pn_b_plus_c>0.35) & (0.96<pn_b_vs_c<=0.99)',
                52: '(pn_b_plus_c>0.35) & (0.88<pn_b_vs_c<=0.96)',
                51: '(pn_b_plus_c>0.35) & (0.70<pn_b_vs_c<=0.88)',
                50: '(pn_b_plus_c>0.35) & (0.40<pn_b_vs_c<=0.70)',

                44: '(pn_b_plus_c>0.35) & (pn_b_vs_c<=0.05)',
                43: '(pn_b_plus_c>0.35) & (0.05<pn_b_vs_c<=0.15)',
                42: '(pn_b_plus_c>0.35) & (0.15<pn_b_vs_c<=0.40)',
                41: '(0.17<pn_b_plus_c<=0.35)',
                40: '(0.1<pn_b_plus_c<=0.17)',

                0: '(pn_b_plus_c<=0.1)',
            }

    def evalJetTag(self, j, default=0):
        for wp, expr in self.jetTagWPs.items():
            if eval(expr, j.__dict__):
                return wp
        return default

    def _cleanObjects(self, event):
        event.ak4jets = []
        for j in event._allJets:
            if not (j.pt > 25 and abs(j.eta) < 2.4 and (j.jetId & 4)):
                # NOTE: ttH(bb) uses jets w/ pT > 30 GeV, loose PU Id
                # pt, eta, tightIdLepVeto, loose PU ID
                continue
            if not self._usePuppiJets and not (j.pt > 50 or j.puId >= self.puID_WP):
                # apply jet puId only for CHS jets
                continue
            if closest(j, event.looseLeptons)[1] < 0.4:
                continue
            j.btagDeepFlavC = j.btagDeepFlavB * j.btagDeepFlavCvB / (
                1 - j.btagDeepFlavCvB) if (j.btagDeepFlavCvB >= 0 and j.btagDeepFlavCvB < 1) else -1
            if self.hasParticleNetAK4 == 'privateNano':
                # attach ParticleNet scores
                j.pn_b = convert_prob(j, ['b', 'bb'], ['c', 'cc', 'uds', 'g'], 'ParticleNetAK4_prob')
                j.pn_c = convert_prob(j, ['c', 'cc'], ['b', 'bb', 'uds', 'g'], 'ParticleNetAK4_prob')
                j.pn_uds = convert_prob(j, 'uds', ['b', 'bb', 'c', 'cc', 'g'], 'ParticleNetAK4_prob')
                j.pn_g = convert_prob(j, 'g', ['b', 'bb', 'c', 'cc', 'uds'], 'ParticleNetAK4_prob')
                j.pn_b_plus_c = j.pn_b + j.pn_c
                j.pn_b_vs_c = j.pn_b / j.pn_b_plus_c
                j.tag = self.evalJetTag(j)
            elif self.hasParticleNetAK4 == 'jmeNano':
                # attach ParticleNet scores
                j.pn_b = j.particleNetAK4_B
                j.pn_c = j.particleNetAK4_B * j.particleNetAK4_CvsB / (
                    1 - j.particleNetAK4_CvsB) if (j.particleNetAK4_CvsB >= 0 and j.particleNetAK4_CvsB < 1) else -1
                j.pn_uds = np.clip(1 - j.pn_b - j.pn_c, 0, 1) * j.particleNetAK4_QvsG if (
                    j.particleNetAK4_QvsG >= 0 and j.particleNetAK4_QvsG < 1) else -1
                j.pn_g = np.clip(1 - j.pn_b - j.pn_c - j.pn_uds, 0, 1) if (
                    j.particleNetAK4_QvsG >= 0 and j.particleNetAK4_QvsG < 1) else -1
                j.pn_b_plus_c = j.pn_b + j.pn_c
                j.pn_b_vs_c = j.pn_b / j.pn_b_plus_c
                j.tag = self.evalJetTag(j)
            else:
                j.tag = 0
