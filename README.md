# Overview

This repository is a minimal example to reproduce an issue with the dependencies of pytorch.

## Steps
```bash
pants generate-lockfiles
pants run run.py
```

On my machine this yields:
```
15:37:02.32 [INFO] Completed: Building 1 requirement for run.py.pex from the python.lock resolve: torch==2.0.0
15:37:02.32 [ERROR] 1 Exception encountered:

Engine traceback:
  in `run` goal

ProcessExecutionFailure: Process 'Building 1 requirement for run.py.pex from the python.lock resolve: torch==2.0.0' failed with exit code 1.
stdout:

stderr:
Failed to resolve requirements from PEX environment @ /home/me/.cache/pants/named_caches/pex_root/unzipped_pexes/2896a51e4b74da2fdbe283e0122b36807e7275ff.
Needed cp38-cp38-manylinux_2_31_x86_64 compatible dependencies for:
 1: nvidia-cuda-nvrtc-cu11==11.7.99; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cuda-nvrtc-cu11', normalized='nvidia-cuda-nvrtc-cu11') distributions.
 2: nvidia-cuda-runtime-cu11==11.7.99; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cuda-runtime-cu11', normalized='nvidia-cuda-runtime-cu11') distributions.
 3: nvidia-cuda-cupti-cu11==11.7.101; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cuda-cupti-cu11', normalized='nvidia-cuda-cupti-cu11') distributions.
 4: nvidia-cudnn-cu11==8.5.0.96; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cudnn-cu11', normalized='nvidia-cudnn-cu11') distributions.
 5: nvidia-cublas-cu11==11.10.3.66; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cublas-cu11', normalized='nvidia-cublas-cu11') distributions.
 6: nvidia-cufft-cu11==10.9.0.58; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cufft-cu11', normalized='nvidia-cufft-cu11') distributions.
 7: nvidia-curand-cu11==10.2.10.91; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-curand-cu11', normalized='nvidia-curand-cu11') distributions.
 8: nvidia-cusolver-cu11==11.4.0.1; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cusolver-cu11', normalized='nvidia-cusolver-cu11') distributions.
 9: nvidia-cusparse-cu11==11.7.4.91; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-cusparse-cu11', normalized='nvidia-cusparse-cu11') distributions.
 10: nvidia-nccl-cu11==2.14.3; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-nccl-cu11', normalized='nvidia-nccl-cu11') distributions.
 11: nvidia-nvtx-cu11==11.7.91; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='nvidia-nvtx-cu11', normalized='nvidia-nvtx-cu11') distributions.
 12: triton==2.0.0; platform_system == "Linux" and platform_machine == "x86_64"
    Required by:
      torch 2.0.0
    But this pex had no ProjectName(raw='triton', normalized='triton') distributions.



Use `--keep-sandboxes=on_failure` to preserve the process chroot for inspection.
```
