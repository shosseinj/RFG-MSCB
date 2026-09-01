# Comparison Table Provenance

This ledger records the values currently copied into Tables 4--8. A status of
`UNVERIFIED` means that the bibliographic identity is known but the exact value and
locator have not yet been checked in an opened primary publication. Missing values are
recorded as `--`; they are not numerical observations. Values were not changed during
this audit solely because a secondary paper reported a different number.

## Source keys

| Method | Primary source |
|---|---|
| CTNet | Xiao et al., *IEEE Transactions on Cybernetics* 54 (2024), 5040--5053, DOI `10.1109/TCYB.2024.3368154` |
| MEGANet | Bui et al., WACV 2024, 7985--7994, DOI `10.1109/WACV57701.2024.00780` |
| CAFE-Net | Liu et al., *Expert Systems with Applications* 238 (2024), 121754, DOI `10.1016/j.eswa.2023.121754` |
| Polyp-LVT | Lin et al., *Knowledge-Based Systems* 300 (2024), 112181, DOI `10.1016/j.knosys.2024.112181` |
| Polyp-Mamba | Zhu et al., *Information Fusion* 115 (2025), 102759, DOI `10.1016/j.inffus.2024.102759` |
| MEIN | Kang et al., *Neural Networks* 189 (2025), 107553, DOI `10.1016/j.neunet.2025.107553` |
| MF-Net | Wang et al., *Expert Systems with Applications* 280 (2025), 127558, DOI `10.1016/j.eswa.2025.127558` |
| MSBP-Net | Pan et al., *Pattern Recognition* 170 (2026), 112101, DOI `10.1016/j.patcog.2025.112101` |
| CIFFormer | Xu et al., *Neurocomputing* 644 (2025), 130413, DOI `10.1016/j.neucom.2025.130413` |
| PFPRNet | Chu et al., *IEEE JBHI* 29(2) (2025), 1137--1150, DOI `10.1109/JBHI.2024.3500026` |
| PraNet-V2 | Hu et al., *Computational Visual Media* 12(2) (2026), 493--500, DOI `10.26599/CVM.2025.9450510` |
| MLB-Net | Ti et al., *Journal of Imaging Informatics in Medicine* (2026), DOI `10.1007/s10278-026-01909-z` |
| MSPN | Yang et al., ICASSP 2026, 7652--7656, DOI `10.1109/ICASSP55912.2026.11461882` |
| DVFIP-Net | Yun et al., *IEEE Access* 14 (2026), 31995--32008, DOI `10.1109/ACCESS.2026.3667956` |

Metric order below is `mDice; mIoU; F_beta^w; S_alpha; mean E; max E; MAE`.

## Kvasir-SEG

| Method | Copied values | Primary locator | Status |
|---|---|---|---|
| CTNet | `0.917; 0.863; 0.910; 0.928; 0.959; 0.964; 0.023` | Exact primary table/page unavailable | UNVERIFIED |
| MEGANet | `0.913; 0.863; 0.907; 0.918; 0.956; 0.959; 0.025` | Exact primary table/page unavailable | UNVERIFIED |
| CAFE-Net | `0.933; 0.889; 0.927; 0.939; 0.967; --; 0.019` | Exact primary table/page unavailable | UNVERIFIED |
| Polyp-LVT | `0.909; 0.851; 0.913; 0.922; 0.941; --; 0.024` | Exact primary table/page unavailable | UNVERIFIED |
| Polyp-Mamba | `0.919; 0.867; 0.912; 0.951; --; 0.968; 0.021` | Exact primary table/page unavailable | UNVERIFIED |
| MEIN | `0.905; 0.847; 0.905; 0.914; --; 0.964; 0.026` | Exact primary table/page unavailable | UNVERIFIED |
| MF-Net | `0.915; 0.863; 0.939; 0.924; 0.962; --; 0.022` | Exact primary table/page unavailable | UNVERIFIED |
| MSBP-Net | `0.919; 0.868; 0.916; 0.926; 0.961; --; 0.023` | Exact primary table/page unavailable | UNVERIFIED |
| CIFFormer | `0.926; 0.876; 0.929; 0.939; 0.967; --; 0.019` | Exact primary table/page unavailable | UNVERIFIED |
| PFPRNet | `0.930; 0.881; 0.920; 0.935; 0.971; --; 0.019` | Exact primary table/page unavailable | UNVERIFIED |
| PraNet-V2 | `0.907; 0.853; --; --; --; --; 0.025` | Exact primary table/page unavailable | UNVERIFIED |
| MLB-Net | `0.926; 0.878; 0.921; 0.938; 0.969; 0.975; 0.021` | Exact primary table/page unavailable | UNVERIFIED |
| MSPN | `0.927; 0.879; --; --; --; --; 0.021` | Exact primary table/page unavailable | UNVERIFIED |
| DVFIP-Net | `0.922; 0.874; --; --; --; --; --` | Exact primary table/page unavailable | UNVERIFIED |

## CVC-ClinicDB

| Method | Copied values | Primary locator | Status |
|---|---|---|---|
| CTNet | `0.936; 0.887; 0.934; 0.952; 0.983; 0.986; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| MEGANet | `0.938; 0.894; 0.940; 0.950; --; 0.987; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| Polyp-Mamba | `0.941; 0.896; 0.936; 0.970; --; 0.970; 0.008` | Exact primary table/page unavailable | UNVERIFIED |
| MEIN | `0.923; 0.878; 0.928; 0.944; --; 0.970; 0.008` | Exact primary table/page unavailable | UNVERIFIED |
| MF-Net | `0.931; 0.884; 0.953; 0.949; 0.983; --; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| MSBP-Net | `0.940; 0.892; 0.927; 0.939; 0.976; --; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| CIFFormer | `0.944; 0.897; 0.941; 0.934; 0.972; --; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| PFPRNet | `0.949; 0.903; 0.947; 0.957; 0.989; --; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| PraNet-V2 | `0.929; 0.880; --; --; --; --; 0.009` | Exact primary table/page unavailable | UNVERIFIED |
| MLB-Net | `0.945; 0.902; 0.948; 0.958; 0.989; 0.992; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| MSPN | `0.943; 0.902; --; --; --; --; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| DVFIP-Net | `0.942; 0.896; --; --; --; --; --` | Primary abstract reports `0.942/0.896`; other metrics unavailable | VERIFIED for mDice/mIoU only |

## ETIS-LaribPolypDB

| Method | Copied values | Primary locator | Status |
|---|---|---|---|
| CTNet | `0.810; 0.734; 0.776; 0.886; 0.913; 0.921; 0.014` | Exact primary table/page unavailable | UNVERIFIED |
| MEGANet | `0.789; 0.709; 0.753; 0.866; 0.855; 0.915; 0.015` | Exact primary table/page unavailable | UNVERIFIED |
| Polyp-Mamba | `0.756; 0.668; 0.756; 0.887; --; 0.872; 0.014` | Exact primary table/page unavailable | UNVERIFIED |
| MEIN | `0.788; 0.711; 0.764; 0.870; --; 0.902; 0.018` | Exact primary table/page unavailable | UNVERIFIED |
| MF-Net | `0.821; 0.750; 0.850; 0.901; 0.925; --; 0.011` | Exact primary table/page unavailable | UNVERIFIED |
| MSBP-Net | `0.795; 0.718; 0.770; 0.873; 0.899; --; 0.019` | Exact primary table/page unavailable | UNVERIFIED |
| CIFFormer | `0.810; 0.746; 0.858; 0.889; 0.918; --; 0.013` | Exact primary table/page unavailable | UNVERIFIED |
| PFPRNet | `0.828; 0.764; 0.839; 0.908; 0.935; --; 0.012` | Exact primary table/page unavailable | UNVERIFIED |
| PraNet-V2 | `0.713; 0.633; --; --; --; --; 0.021` | Exact primary table/page unavailable | UNVERIFIED |
| MLB-Net | `0.821; 0.744; 0.780; 0.899; 0.914; 0.935; 0.013` | Exact primary table/page unavailable | UNVERIFIED |
| MSPN | `0.798; 0.717; --; --; --; --; 0.017` | Exact primary table/page unavailable | UNVERIFIED |
| DVFIP-Net | `0.811; 0.730; --; --; --; --; --` | Exact primary table/page unavailable | UNVERIFIED |

## CVC-ColonDB

| Method | Copied values | Primary locator | Status |
|---|---|---|---|
| CTNet | `0.813; 0.734; 0.801; 0.874; 0.915; 0.919; 0.040` | Exact primary table/page unavailable | UNVERIFIED |
| MEGANet | `0.793; 0.714; 0.779; 0.854; 0.892; 0.895; 0.034` | Exact primary table/page unavailable | UNVERIFIED |
| Polyp-Mamba | `0.791; 0.713; 0.765; 0.846; --; 0.902; 0.034` | Exact primary table/page unavailable | UNVERIFIED |
| MEIN | `0.791; 0.715; 0.785; 0.856; --; 0.897; 0.034` | Exact primary table/page unavailable | UNVERIFIED |
| MF-Net | `0.825; 0.751; 0.864; 0.887; 0.929; --; 0.024` | Exact primary table/page unavailable | UNVERIFIED |
| MSBP-Net | `0.810; 0.731; 0.810; 0.861; 0.912; --; 0.029` | Exact primary table/page unavailable | UNVERIFIED |
| CIFFormer | `0.823; 0.741; 0.851; 0.874; 0.918; --; 0.026` | Exact primary table/page unavailable | UNVERIFIED |
| PFPRNet | `0.819; 0.741; 0.843; 0.882; 0.915; --; 0.028` | Exact primary table/page unavailable | UNVERIFIED |
| PraNet-V2 | `0.702; 0.620; --; --; --; --; 0.044` | Exact primary table/page unavailable | UNVERIFIED |
| MLB-Net | `0.832; 0.757; 0.825; 0.886; 0.924; 0.931; 0.023` | Exact primary table/page unavailable | UNVERIFIED |
| MSPN | `0.811; 0.734; --; --; --; --; 0.029` | Exact primary table/page unavailable | UNVERIFIED |
| DVFIP-Net | `0.826; 0.746; --; --; --; --; --` | Primary abstract reports `0.826/0.746`; other metrics unavailable | VERIFIED for mDice/mIoU only |

## CVC-300

| Method | Copied values | Primary locator | Status |
|---|---|---|---|
| CTNet | `0.908; 0.844; 0.894; 0.975; 0.975; 0.982; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| MEGANet | `0.899; 0.834; 0.882; 0.935; 0.966; 0.969; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| Polyp-Mamba | `0.906; 0.840; 0.888; 0.936; --; 0.975; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| MEIN | `0.893; 0.828; 0.880; 0.930; --; 0.965; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| MF-Net | `0.897; 0.836; 0.918; 0.941; 0.966; --; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| MSBP-Net | `0.903; 0.859; 0.927; 0.942; 0.967; --; 0.019` | Exact primary table/page unavailable | UNVERIFIED |
| CIFFormer | `0.883; 0.822; 0.912; 0.939; 0.961; --; 0.100` | Exact primary table/page unavailable; `0.100` requires source confirmation | UNVERIFIED / SUSPICIOUS |
| PFPRNet | `0.891; 0.833; 0.917; 0.928; 0.950; --; 0.013` | Exact primary table/page unavailable | UNVERIFIED |
| PraNet-V2 | `0.873; 0.795; --; --; --; --; 0.007` | Exact primary table/page unavailable | UNVERIFIED |
| MLB-Net | `0.915; 0.852; 0.909; 0.974; 0.974; 0.978; 0.005` | Exact primary table/page unavailable | UNVERIFIED |
| MSPN | `0.907; 0.840; --; --; --; --; 0.006` | Exact primary table/page unavailable | UNVERIFIED |
| DVFIP-Net | `0.900; 0.833; --; --; --; --; --` | Exact primary table/page unavailable | UNVERIFIED |
