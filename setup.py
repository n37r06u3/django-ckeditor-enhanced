from setuptools import setup, find_packages

setup(
    name = 'django-ckeditor-enhanced',
    version = '1.4',
    keywords = ('django','ckeditor'),
    description = 'django-ckeditor-updated with codesnippet plugin support',

    url = 'https://github.com/n37r06u3/django-ckeditor-enhanced',
    author = 'n37r06u3',
    author_email = 'n37r06u3@gmail.com',

    platforms = 'any',
    packages=find_packages(),
    
    install_requires=[
                      'Django',
                      ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)