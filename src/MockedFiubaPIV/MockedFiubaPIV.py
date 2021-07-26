from random import gauss

import PIL.Image


class MockedFiubaPIV:
    def __init__(self):
        print('initin fiuba piv')

    def piv(self, data: dict) -> dict:
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
            1: (<PIL.Image.Image image mode=P size=512x512 at 0x7F6397AF1FA0>, <PIL.Image.Image image mode=P size=512x512 at 0x7F6397AF1F70>),  # noqa: E501
            2: (<PIL.Image.Image image mode=P size=512x512 at 0x7F63B031C820>, <PIL.Image.Image image mode=P size=512x512 at 0x7F6397AE8F40>),  # noqa: E501
            3: (<PIL.Image.Image image mode=P size=512x512 at 0x7F6397AE8820>, <PIL.Image.Image image mode=P size=512x512 at 0x7F6397AE8400>)}, # noqa: E501
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

        return value: the return value is a dict with velocities for all markers.
        Velocities come expressed in vectorial decomposition and their magnitudes.
        result: dict with k=marker_id, v=dict with keys 'vel_x', 'vel_y', vel_magnitude'
        sample result:
        {
            1: {'vel_x': 10.919442112521295, 'vel_y': 11.024498299102545, 'vel_magnitude': 13.15307101517097},
            2: {'vel_x': 9.327311460265268, 'vel_y': 10.102254321525308, 'vel_magnitude': 13.859931914939187},
            3: {'vel_x': 13.146793839557047, 'vel_y': 7.310334773247977, 'vel_magnitude': 10.263030664829332}
        }
        """
        result = {}
        for key, value in data['imgs'].items():
            result[key] = self.get_piv_for(value[0], value[1])
        return result

    def get_piv_for(self, img1: PIL.Image.Image, img2: PIL.Image.Image) -> dict:
        vel_x = gauss(10, 2)
        vel_y = gauss(10, 2)
        vel_magnitude = gauss(10, 2)
        return {"vel_x": vel_x, "vel_y": vel_y, "vel_magnitude": vel_magnitude}
