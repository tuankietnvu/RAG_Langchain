import os
import wget

file_links = [
    {
        "title": "Attention Is All You Need",
        "url": "https://arxiv.org/pdf/1706.03762"
    },
    {
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "url": "https://arxiv.org/pdf/1810.04805"
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/pdf/2201.11903"
    },
    {
        "title": "Language Models are Few-Shot Learners",
        "url": "https://arxiv.org/pdf/2005.14165"
    },
    {
        "title": "Scaling Laws for Neural Language Models",
        "url": "https://arxiv.org/pdf/2001.08361"
    },
    {
        "title": "Self-Attention with Functional Time Complexity",
        "url": "https://arxiv.org/pdf/2009.04758"
    },
    {
        "title": "The Power of Scale for Parameter-Efficient Prompt Tuning",
        "url": "https://arxiv.org/pdf/2104.08691"
    },
    {
        "title": "Denoising Diffusion Probabilistic Models",
        "url": "https://arxiv.org/pdf/2006.11239"
    },
    {
        "title": "Instruction Tuning for Language Models- A Survey",
        "url": "https://arxiv.org/pdf/2308.10792"
    },
    {
        "title": "Llama 2- Open Foundation and Fine-Tuned Chat Models",
        "url": "https://arxiv.org/pdf/2307.09288"
    }
]

def is_exist(file_link):
    return os.path.exists(f"./{file_link["title"]}.pdf")

for file_link in file_links:
    if not is_exist(file_link):
        print(f"Downloading {file_link['title']}...")
        try:
            wget.download(file_link["url"], out=f"./{file_link['title']}.pdf")
            print(f"\nDownloaded {file_link['title']}")
        except Exception as e:
            print(f"Failed to download {file_link['title']}: {e}")
    else:
        print(f"{file_link['title']} already exists.")