{
	'conditions': [
		['OS=="win"', {
			'variables': {
				'copy_command%': 'copy',
				'module_name%': 'gdt-steam-win',
				'redist_bin_dir%': '',
				'lib_extension%': 'dll'
			},
		}],

		['OS=="mac"', {
			'variables': {
				'copy_command%': 'cp',
				'module_name%': 'gdt-steam-osx',
				'redist_bin_dir%': 'osx32',
				'lib_extension%': 'dylib'
			},
		}],

		['OS=="linux"', {
			'variables': {
				'copy_command%': 'cp',
				'module_name%': 'gdt-steam-linux',
				'redist_bin_dir%': 'linux32',
				'lib_extension%': 'so'
			},
		}]
	],
	
	'targets': [
		{
			'target_name': 'gdt-steam',
			'sources': [ 
				'main.cpp'
			],
			'link_settings': {
				'ldflags': ['-L$(CURDIR)/../steamworks-sdk/redistributable_bin/<(redist_bin_dir)'],
				'libraries': [
					'$(CURDIR)/../steamworks-sdk/redistributable_bin/<(redist_bin_dir)/libsteam_api.<(lib_extension)'
				]
			}
		},

		{
			'target_name': 'action_after_build',
			'type': 'none',
			'actions': [
				{
					'action_name': 'move_node_module',

					'inputs': [
						'<@(PRODUCT_DIR)/gdt-steam.node'
					],

					'outputs': [
						'deploy/<@(module_name).node'
					],

					'action': ['<@(copy_command)', '<@(PRODUCT_DIR)/gdt-steam.node', 'deploy/<@(module_name).node']
				}
			]
		}
	]
}
