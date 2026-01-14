from setuptools import setup, find_packages
from typing import List
import os


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from a requirements file.
    
    Args:
        file_path (str): Path to the requirements file
        
    Returns:
        List[str]: List of package requirements
        
    Raises:
        FileNotFoundError: If the requirements file doesn't exist
        IOError: If there's an error reading the file
    """
    HYPHEN_E_DOT = "-e ."
    requirements = []
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Requirements file not found: {file_path}")
            
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            requirements = file_obj.readlines()
            
        # Clean up requirements: strip whitespace and filter out empty lines
        requirements = [
            req.strip() 
            for req in requirements 
            if req.strip() and not req.strip().startswith('#')
        ]
        
        # Remove editable install marker if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    except IOError as e:
        raise IOError(f"Error reading requirements file {file_path}: {e}")
        
    return requirements


# Read long description from README if available
def get_long_description() -> str:
    """Get long description from README file."""
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


setup(
    name='my_package',
    version='0.0.1',
    author='Rajath',
    author_email='rajathdsu@gmail.com',  # Fixed: Added quotes around email
    description='A Python package for data science tasks',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/username/my_package',  # Add your repository URL
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=get_requirements('requirements.txt'),  # Use dynamic requirements
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
            'mypy>=0.800',
        ],
        'docs': [
            'sphinx>=4.0',
            'sphinx-rtd-theme>=0.5',
        ],
    },
    entry_points={
        'console_scripts': [
            # 'my_package=my_package.cli:main',  # Uncomment if you have CLI
        ],
    },
    include_package_data=True,
    zip_safe=False,
)