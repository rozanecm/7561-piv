class MockedFiubaPIV:
    def __init__(self):
        print('initin fiuba piv')

    def piv(self, data: dict):
        """
        data: { 'imgs': dict with k: marker_id, v: tuple of (left, right) imgs,
                'settings': {
                    'delta_t': int,
                    'ppm': int,
                    'roi': int,
                    'selection_size': int,
                    'markers': dict with k: marker_id, v: dict with "position_x" and "position_y" keys
            }
        sample data:
        {'imgs': {
            1: (<PIL.Image.Image image mode=P size=512x512 at 0x7F6397AF1FA0>, <PIL.Image.Image image mode=P size=512x512 at 0x7F6397AF1F70>),
            2: (<PIL.Image.Image image mode=P size=512x512 at 0x7F63B031C820>, <PIL.Image.Image image mode=P size=512x512 at 0x7F6397AE8F40>),
            3: (<PIL.Image.Image image mode=P size=512x512 at 0x7F6397AE8820>, <PIL.Image.Image image mode=P size=512x512 at 0x7F6397AE8400>)},
        'settings': {
            'delta_t': 1,
            'ppm': 1,
            'roi': 512,
            'selection_size': 8,
            'markers': {
                1: {'position_x': 425, 'position_y': 486},
                2: {'position_x': 599, 'position_y': 783},
                3: {'position_x': 559, 'position_y': 119}}
            }
        }
        """
        print(data)
