# COLORS RGB
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (220, 220, 220),
    "BG_GREEN": (20, 90, 45),
    "GREEN": (0, 128, 0),
    "ROBOT_BLACK": (25, 25, 25),
    "ORANGE": (253, 106, 2),
    "BLUE": (0, 64, 255),
    "YELLOW": (250, 218, 94),
    "GREEN": (57, 220, 20),
    "RED": (151, 21, 0),
    "PURPLE": (102, 51, 153),
    "PINK": (220, 0, 220),
}

TAG_ID_COLORS = {
    0: {
        0: COLORS["PINK"],
        1: COLORS["GREEN"],
        2: COLORS["PINK"],
        3: COLORS["PINK"],
    },
    1: {
        0: COLORS["GREEN"],
        1: COLORS["GREEN"],
        2: COLORS["PINK"],
        3: COLORS["PINK"],
    },
    2: {
        0: COLORS["GREEN"],
        1: COLORS["GREEN"],
        2: COLORS["PINK"],
        3: COLORS["GREEN"],
    },
    3: {
        0: COLORS["PINK"],
        1: COLORS["GREEN"],
        2: COLORS["PINK"],
        3: COLORS["GREEN"],
    },
    4: {
        0: COLORS["PINK"],
        1: COLORS["PINK"],
        2: COLORS["GREEN"],
        3: COLORS["PINK"],
    },
    5: {
        0: COLORS["GREEN"],
        1: COLORS["PINK"],
        2: COLORS["GREEN"],
        3: COLORS["PINK"],
    },
    6: {
        0: COLORS["GREEN"],
        1: COLORS["PINK"],
        2: COLORS["GREEN"],
        3: COLORS["GREEN"],
    },
    7: {
        0: COLORS["PINK"],
        1: COLORS["PINK"],
        2: COLORS["GREEN"],
        3: COLORS["GREEN"],
    },
    8: {
        0: COLORS["GREEN"],
        1: COLORS["GREEN"],
        2: COLORS["GREEN"],
        3: COLORS["GREEN"],
    },
    9: {
        0: COLORS["PINK"],
        1: COLORS["PINK"],
        2: COLORS["PINK"],
        3: COLORS["PINK"],
    },
    10: {
        0: COLORS["PINK"],
        1: COLORS["GREEN"],
        2: COLORS["GREEN"],
        3: COLORS["PINK"],
    },
    11: {
        0: COLORS["GREEN"],
        1: COLORS["PINK"],
        2: COLORS["PINK"],
        3: COLORS["GREEN"],
    },
    12: {
        0: COLORS["GREEN"],
        1: COLORS["GREEN"],
        2: COLORS["GREEN"],
        3: COLORS["PINK"],
    },
    13: {
        0: COLORS["GREEN"],
        1: COLORS["PINK"],
        2: COLORS["PINK"],
        3: COLORS["PINK"],
    },
    14: {
        0: COLORS["PINK"],
        1: COLORS["GREEN"],
        2: COLORS["GREEN"],
        3: COLORS["GREEN"],
    },
    15: {
        0: COLORS["PINK"],
        1: COLORS["PINK"],
        2: COLORS["PINK"],
        3: COLORS["GREEN"],
    },
}

VISION_COLORS = {
    "ORANGE": [255, 128, 0],  
    "BLUE": [0, 0, 255],   
    "YELLOW": [255, 255, 0], 
    "RED": [255, 0, 0],    
    "GREEN": [0, 255, 0],    
    "PINK": [255, 0, 255],   
    "CYAN": [0, 255, 255], 
}

VISION_IDS_COLORS_MAP = {
    0: [VISION_COLORS["RED"], VISION_COLORS["GREEN"]],
    1: [VISION_COLORS["RED"], VISION_COLORS["PINK"]],
    2: [VISION_COLORS["RED"], VISION_COLORS["CYAN"]],
    3: [VISION_COLORS["GREEN"], VISION_COLORS["RED"]],
    4: [VISION_COLORS["GREEN"], VISION_COLORS["PINK"]],
    5: [VISION_COLORS["GREEN"], VISION_COLORS["CYAN"]],
    6: [VISION_COLORS["PINK"], VISION_COLORS["RED"]],
    7: [VISION_COLORS["PINK"], VISION_COLORS["GREEN"]],
    8: [VISION_COLORS["PINK"], VISION_COLORS["CYAN"]],
    9: [VISION_COLORS["CYAN"], VISION_COLORS["RED"]],
    10: [VISION_COLORS["CYAN"], VISION_COLORS["GREEN"]],
    11: [VISION_COLORS["CYAN"], VISION_COLORS["PINK"]]
}