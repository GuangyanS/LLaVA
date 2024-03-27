import os
from llava.train.train import train

if __name__ == "__main__":
    os.environ["WANDB_PROJECT"]="LLaVA"
    train(attn_implementation="flash_attention_2")
