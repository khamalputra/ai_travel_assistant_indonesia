from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-travel-assistant-indonesia",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI Travel Assistant untuk traveler Indonesia dengan LangChain dan Google Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-travel-assistant-indonesia",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "travel-assistant=travel_assistant_with_langchain:main",
        ],
    },
    keywords="ai, travel, assistant, indonesia, langchain, gemini, streamlit",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ai-travel-assistant-indonesia/issues",
        "Source": "https://github.com/yourusername/ai-travel-assistant-indonesia",
        "Documentation": "https://github.com/yourusername/ai-travel-assistant-indonesia/docs",
    },
)
