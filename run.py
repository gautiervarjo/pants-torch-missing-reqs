import torch


if __name__ == "__main__":
    assert torch.cuda.is_available()
    print("Torch version", torch.__version__)
    print("Arch list", torch.cuda.get_arch_list())
