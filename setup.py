from setuptools import setup, find_packages



setup(
	name='typeidea',
	version='0.1',
	description='Blog System base on Django',
	author='thephoenix-sy',
	author_email='423599771@qq.com',
	license='MIT',
	packages=find_packages('typeidea'),
	package_dir={'': 'typeidea'},
	include_package_data=True,
	install_requires=[
		'django~=1.11',
	],
	extras_require={
		'ipython': ['ipython==6.2.1']
	},
	scripts=[
		'typeidea/manage.py',
	],
	entry_points={
		'console_scripts': [
			'typeidea_manage = manage:main',
		]
	},
	classifiers=[    #   Optional
		#软件成熟度如何？一般有下面几个选项
		#  3 - Alpha
		#  4 - Beta
		#  5 - Production/Stable
		'Development Status  ::  3 - Alpha',

		#指明项目的受众
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Libraries',

		#选择项目的许可证
		'License :: OSI Approved :: MIT License',

		#指定项需要实用的python版本
		'Programming Language :: Python :: 3.6',
	],
)