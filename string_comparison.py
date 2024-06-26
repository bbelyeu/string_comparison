"""
String comparison main module.

This maps a Unicode code point key represented as an integer to a corresponding ASCII
character mapping. In some cases such as Hebrew niqqud & cantillation, we remove the
character altogether or replace certain punctuation with a space.

In addition, some characters are removed prior to normalization. For example, Unicode control chars.
"""

import unicodedata

UNICODE = {
    0: "",
    171: '"',
    173: "-",
    178: "2",
    179: "3",
    185: "1",
    187: '"',
    192: "A",
    193: "A",
    194: "A",
    195: "A",
    196: "A",
    197: "A",
    198: "AE",
    199: "C",
    200: "E",
    201: "E",
    202: "E",
    203: "E",
    204: "I",
    205: "I",
    206: "I",
    207: "I",
    208: "D",
    209: "N",
    210: "O",
    211: "O",
    212: "O",
    213: "O",
    214: "O",
    216: "O",
    217: "U",
    218: "U",
    219: "U",
    220: "U",
    221: "Y",
    222: "TH",
    223: "ss",
    224: "a",
    225: "a",
    226: "a",
    227: "a",
    228: "a",
    229: "a",
    230: "ae",
    231: "c",
    232: "e",
    233: "e",
    234: "e",
    235: "e",
    236: "i",
    237: "i",
    238: "i",
    239: "i",
    240: "d",
    241: "n",
    242: "o",
    243: "o",
    244: "o",
    245: "o",
    246: "o",
    248: "o",
    249: "u",
    250: "u",
    251: "u",
    252: "u",
    253: "y",
    254: "th",
    255: "y",
    256: "A",
    257: "a",
    258: "A",
    259: "a",
    260: "A",
    261: "a",
    262: "C",
    263: "c",
    264: "C",
    265: "c",
    266: "C",
    267: "c",
    268: "C",
    269: "c",
    270: "D",
    271: "d",
    272: "D",
    273: "d",
    274: "E",
    275: "e",
    276: "E",
    277: "e",
    278: "E",
    279: "e",
    280: "E",
    281: "e",
    282: "E",
    283: "e",
    284: "G",
    285: "g",
    286: "G",
    287: "g",
    288: "G",
    289: "g",
    290: "G",
    291: "g",
    292: "H",
    293: "h",
    294: "H",
    295: "h",
    296: "I",
    297: "i",
    298: "I",
    299: "i",
    300: "I",
    301: "i",
    302: "I",
    303: "i",
    304: "I",
    305: "i",
    306: "IJ",
    307: "ij",
    308: "J",
    309: "j",
    310: "K",
    311: "k",
    312: "q",
    313: "L",
    314: "l",
    315: "L",
    316: "l",
    317: "L",
    318: "l",
    319: "L",
    320: "l",
    321: "L",
    322: "l",
    323: "N",
    324: "n",
    325: "N",
    326: "n",
    327: "N",
    328: "n",
    329: "n",
    330: "N",
    331: "n",
    332: "O",
    333: "o",
    334: "O",
    335: "o",
    336: "O",
    337: "o",
    338: "OE",
    339: "oe",
    340: "R",
    341: "r",
    342: "R",
    343: "r",
    344: "R",
    345: "r",
    346: "S",
    347: "s",
    348: "S",
    349: "s",
    350: "S",
    351: "s",
    352: "S",
    353: "s",
    354: "T",
    355: "t",
    356: "T",
    357: "t",
    358: "T",
    359: "t",
    360: "U",
    361: "u",
    362: "U",
    363: "u",
    364: "U",
    365: "u",
    366: "U",
    367: "u",
    368: "U",
    369: "u",
    370: "U",
    371: "u",
    372: "W",
    373: "w",
    374: "Y",
    375: "y",
    376: "Y",
    377: "Z",
    378: "z",
    379: "Z",
    380: "z",
    381: "Z",
    382: "z",
    383: "s",
    384: "b",
    385: "B",
    386: "B",
    387: "b",
    390: "O",
    391: "C",
    392: "c",
    393: "D",
    394: "D",
    395: "D",
    396: "d",
    398: "E",
    399: "A",
    400: "E",
    401: "F",
    402: "f",
    403: "G",
    405: "hv",
    406: "I",
    407: "I",
    408: "K",
    409: "k",
    410: "l",
    412: "M",
    413: "N",
    414: "n",
    415: "O",
    416: "O",
    417: "o",
    420: "P",
    421: "p",
    427: "t",
    428: "T",
    429: "t",
    430: "T",
    431: "U",
    432: "u",
    434: "V",
    435: "Y",
    436: "y",
    437: "Z",
    438: "z",
    447: "w",
    452: "DZ",
    453: "Dz",
    454: "dz",
    455: "LJ",
    456: "Lj",
    457: "lj",
    458: "NJ",
    459: "Nj",
    460: "nj",
    461: "A",
    462: "a",
    463: "I",
    464: "i",
    465: "O",
    466: "o",
    467: "U",
    468: "u",
    469: "U",
    470: "u",
    471: "U",
    472: "u",
    473: "U",
    474: "u",
    475: "U",
    476: "u",
    477: "e",
    478: "A",
    479: "a",
    480: "A",
    481: "a",
    482: "AE",
    483: "ae",
    484: "G",
    485: "G",
    486: "G",
    487: "G",
    488: "K",
    489: "k",
    490: "O",
    491: "o",
    492: "O",
    493: "o",
    496: "j",
    497: "DZ",
    498: "Dz",
    499: "dz",
    500: "G",
    501: "g",
    502: "HV",
    503: "W",
    504: "N",
    505: "n",
    506: "A",
    507: "a",
    508: "AE",
    509: "ae",
    510: "O",
    511: "o",
    512: "A",
    513: "a",
    514: "A",
    515: "a",
    516: "E",
    517: "e",
    518: "E",
    519: "e",
    520: "I",
    521: "i",
    522: "I",
    523: "i",
    524: "O",
    525: "o",
    526: "O",
    527: "o",
    528: "R",
    529: "r",
    530: "R",
    531: "r",
    532: "U",
    533: "u",
    534: "U",
    535: "u",
    536: "S",
    537: "s",
    538: "T",
    539: "t",
    540: "Z",
    541: "z",
    542: "H",
    543: "h",
    544: "N",
    545: "d",
    546: "OU",
    547: "ou",
    548: "Z",
    549: "z",
    550: "A",
    551: "a",
    552: "E",
    553: "e",
    554: "O",
    555: "o",
    556: "O",
    557: "o",
    558: "O",
    559: "o",
    560: "O",
    561: "o",
    562: "Y",
    563: "y",
    564: "l",
    565: "n",
    566: "t",
    567: "j",
    568: "db",
    569: "qp",
    570: "A",
    571: "C",
    572: "c",
    573: "L",
    574: "T",
    575: "s",
    576: "z",
    579: "B",
    580: "U",
    581: "V",
    582: "E",
    583: "e",
    584: "J",
    585: "j",
    586: "Q",
    587: "q",
    588: "R",
    589: "r",
    590: "Y",
    591: "y",
    592: "a",
    595: "b",
    596: "o",
    597: "c",
    598: "d",
    599: "d",
    600: "e",
    601: "a",
    602: "a",
    603: "e",
    604: "e",
    605: "e",
    606: "e",
    607: "j",
    608: "g",
    609: "g",
    610: "G",
    613: "h",
    614: "h",
    616: "i",
    618: "I",
    619: "l",
    620: "l",
    621: "l",
    623: "m",
    624: "m",
    625: "m",
    626: "n",
    627: "n",
    628: "N",
    629: "o",
    630: "OE",
    636: "r",
    637: "r",
    638: "r",
    639: "r",
    640: "R",
    641: "R",
    642: "s",
    644: "j",
    647: "t",
    648: "t",
    649: "u",
    651: "v",
    652: "v",
    653: "w",
    654: "y",
    655: "Y",
    656: "z",
    657: "z",
    663: "C",
    665: "B",
    666: "e",
    667: "G",
    668: "H",
    669: "j",
    670: "k",
    671: "L",
    672: "q",
    675: "dz",
    677: "dz",
    678: "ts",
    680: "tc",
    682: "ls",
    683: "lz",
    686: "h",
    687: "h",
    1425: "",
    1426: "",
    1427: "",
    1428: "",
    1429: "",
    1430: "",
    1431: "",
    1432: "",
    1433: "",
    1434: "",
    1435: "",
    1439: "",
    1440: "",
    1441: "",
    1443: "",
    1444: "",
    1445: "",
    1446: "",
    1447: "",
    1448: "",
    1449: "",
    1450: "",
    1451: "",
    1452: "",
    1453: "",
    1454: "",
    1456: "",
    1457: "",
    1458: "",
    1459: "",
    1460: "",
    1461: "",
    1462: "",
    1463: "",
    1464: "",
    1465: "",
    1467: "",
    1468: "",
    1469: "",
    1470: " ",
    1472: " ",
    1473: "",
    1474: "",
    1475: " ",
    7424: "A",
    7425: "AE",
    7426: "ae",
    7427: "B",
    7428: "C",
    7429: "D",
    7430: "D",
    7431: "E",
    7432: "e",
    7433: "i",
    7434: "J",
    7435: "K",
    7436: "L",
    7437: "M",
    7438: "N",
    7439: "O",
    7440: "O",
    7444: "oe",
    7445: "OU",
    7446: "o",
    7447: "o",
    7448: "P",
    7449: "R",
    7450: "R",
    7451: "T",
    7452: "U",
    7456: "V",
    7457: "W",
    7458: "Z",
    7522: "i",
    7523: "r",
    7524: "u",
    7525: "v",
    7531: "ue",
    7532: "b",
    7533: "d",
    7534: "f",
    7535: "m",
    7536: "n",
    7537: "p",
    7538: "r",
    7539: "r",
    7540: "s",
    7541: "t",
    7542: "z",
    7543: "g",
    7545: "g",
    7546: "th",
    7547: "I",
    7548: "i",
    7549: "p",
    7550: "U",
    7552: "b",
    7553: "d",
    7554: "f",
    7555: "g",
    7556: "k",
    7557: "l",
    7558: "m",
    7559: "n",
    7560: "p",
    7561: "r",
    7562: "s",
    7564: "v",
    7565: "x",
    7566: "z",
    7567: "a",
    7569: "d",
    7570: "e",
    7571: "e",
    7572: "e",
    7573: "a",
    7574: "i",
    7575: "o",
    7577: "u",
    7680: "A",
    7681: "a",
    7682: "B",
    7683: "b",
    7684: "B",
    7685: "b",
    7686: "B",
    7687: "b",
    7688: "C",
    7689: "c",
    7690: "D",
    7691: "d",
    7692: "D",
    7693: "d",
    7694: "D",
    7695: "d",
    7696: "D",
    7697: "d",
    7698: "D",
    7699: "d",
    7700: "E",
    7701: "e",
    7702: "E",
    7703: "e",
    7704: "E",
    7705: "e",
    7706: "E",
    7707: "e",
    7708: "E",
    7709: "e",
    7710: "F",
    7711: "f",
    7712: "G",
    7713: "g",
    7714: "H",
    7715: "h",
    7716: "H",
    7717: "h",
    7718: "H",
    7719: "h",
    7720: "H",
    7721: "h",
    7722: "H",
    7723: "h",
    7724: "I",
    7725: "i",
    7726: "I",
    7727: "i",
    7728: "K",
    7729: "k",
    7730: "K",
    7731: "k",
    7732: "K",
    7733: "k",
    7734: "L",
    7735: "l",
    7736: "L",
    7737: "l",
    7738: "L",
    7739: "l",
    7740: "L",
    7741: "l",
    7742: "M",
    7743: "m",
    7744: "M",
    7745: "m",
    7746: "M",
    7747: "m",
    7748: "N",
    7749: "n",
    7750: "N",
    7751: "n",
    7752: "N",
    7753: "n",
    7754: "N",
    7755: "n",
    7756: "O",
    7757: "o",
    7758: "O",
    7759: "o",
    7760: "O",
    7761: "o",
    7762: "O",
    7763: "o",
    7764: "P",
    7765: "p",
    7766: "P",
    7767: "p",
    7768: "R",
    7769: "r",
    7770: "R",
    7771: "r",
    7772: "R",
    7773: "r",
    7774: "R",
    7775: "r",
    7776: "S",
    7777: "s",
    7778: "S",
    7779: "s",
    7780: "S",
    7781: "s",
    7782: "S",
    7783: "s",
    7784: "S",
    7785: "s",
    7786: "T",
    7787: "t",
    7788: "T",
    7789: "t",
    7790: "T",
    7791: "t",
    7792: "T",
    7793: "t",
    7794: "U",
    7795: "u",
    7796: "U",
    7797: "u",
    7798: "U",
    7799: "u",
    7800: "U",
    7801: "u",
    7802: "U",
    7803: "u",
    7804: "V",
    7805: "v",
    7806: "V",
    7807: "v",
    7808: "W",
    7809: "w",
    7810: "W",
    7811: "w",
    7812: "W",
    7813: "w",
    7814: "W",
    7815: "w",
    7816: "W",
    7817: "w",
    7818: "X",
    7819: "x",
    7820: "X",
    7821: "x",
    7822: "Y",
    7823: "y",
    7824: "Z",
    7825: "z",
    7826: "Z",
    7827: "z",
    7828: "Z",
    7829: "z",
    7830: "h",
    7831: "t",
    7832: "w",
    7833: "y",
    7834: "a",
    7835: "f",
    7836: "s",
    7837: "s",
    7838: "SS",
    7840: "A",
    7841: "a",
    7842: "A",
    7843: "a",
    7844: "A",
    7845: "a",
    7846: "A",
    7847: "a",
    7848: "A",
    7849: "a",
    7850: "A",
    7851: "a",
    7852: "A",
    7853: "a",
    7854: "A",
    7855: "a",
    7856: "A",
    7857: "a",
    7858: "A",
    7859: "a",
    7860: "A",
    7861: "a",
    7862: "A",
    7863: "a",
    7864: "E",
    7865: "e",
    7866: "E",
    7867: "e",
    7868: "E",
    7869: "e",
    7870: "E",
    7871: "e",
    7872: "E",
    7873: "e",
    7874: "E",
    7875: "e",
    7876: "E",
    7877: "e",
    7878: "E",
    7879: "e",
    7880: "I",
    7881: "i",
    7882: "I",
    7883: "i",
    7884: "O",
    7885: "o",
    7886: "O",
    7887: "o",
    7888: "O",
    7889: "o",
    7890: "O",
    7891: "o",
    7892: "O",
    7893: "o",
    7894: "O",
    7895: "o",
    7896: "O",
    7897: "o",
    7898: "O",
    7899: "o",
    7900: "O",
    7901: "o",
    7902: "O",
    7903: "o",
    7904: "O",
    7905: "o",
    7906: "O",
    7907: "o",
    7908: "U",
    7909: "u",
    7910: "U",
    7911: "u",
    7912: "U",
    7913: "u",
    7914: "U",
    7915: "u",
    7916: "U",
    7917: "u",
    7918: "U",
    7919: "u",
    7920: "U",
    7921: "u",
    7922: "Y",
    7923: "y",
    7924: "Y",
    7925: "y",
    7926: "Y",
    7927: "y",
    7928: "Y",
    7929: "y",
    7930: "LL",
    7931: "ll",
    7932: "V",
    7934: "Y",
    7935: "y",
    8208: "-",
    8209: "-",
    8210: "-",
    8211: "-",
    8212: "-",
    8216: "'",
    8217: "'",
    8218: "'",
    8219: "'",
    8220: '"',
    8221: '"',
    8222: '"',
    8242: "'",
    8243: '"',
    8245: "'",
    8246: '"',
    8248: "^",
    8249: "'",
    8250: "'",
    8252: "!!",
    8260: "/",
    8261: "[",
    8262: "]",
    8263: "??",
    8264: "?!",
    8265: "!?",
    8270: "*",
    8271: ";",
    8274: "%",
    8275: "~",
    8304: "0",
    8305: "i",
    8308: "4",
    8309: "5",
    8310: "6",
    8311: "7",
    8312: "8",
    8313: "9",
    8314: "+",
    8315: "-",
    8316: "=",
    8317: "(",
    8318: ")",
    8319: "n",
    8320: "0",
    8321: "1",
    8322: "2",
    8323: "3",
    8324: "4",
    8325: "5",
    8326: "6",
    8327: "7",
    8328: "8",
    8329: "9",
    8330: "+",
    8331: "-",
    8332: "=",
    8333: "(",
    8334: ")",
    8336: "a",
    8337: "e",
    8338: "o",
    8339: "x",
    8340: "a",
    8580: "c",
    9312: "1",
    9313: "2",
    9314: "3",
    9315: "4",
    9316: "5",
    9317: "6",
    9318: "7",
    9319: "8",
    9320: "9",
    9321: "10",
    9322: "11",
    9323: "12",
    9324: "13",
    9325: "14",
    9326: "15",
    9327: "16",
    9328: "17",
    9329: "18",
    9330: "19",
    9331: "20",
    9332: "(1)",
    9333: "(2)",
    9334: "(3)",
    9335: "(4)",
    9336: "(5)",
    9337: "(6)",
    9338: "(7)",
    9339: "(8)",
    9340: "(9)",
    9341: "(10)",
    9342: "(11)",
    9343: "(12)",
    9344: "(13)",
    9345: "(14)",
    9346: "(15)",
    9347: "(16)",
    9348: "(17)",
    9349: "(18)",
    9350: "(19)",
    9351: "(20)",
    9352: "1.",
    9353: "2.",
    9354: "3.",
    9355: "4.",
    9356: "5.",
    9357: "6.",
    9358: "7.",
    9359: "8.",
    9360: "9.",
    9361: "10.",
    9362: "11.",
    9363: "12.",
    9364: "13.",
    9365: "14.",
    9366: "15.",
    9367: "16.",
    9368: "17.",
    9369: "18.",
    9370: "19.",
    9371: "20.",
    9372: "(a)",
    9373: "(b)",
    9374: "(c)",
    9375: "(d)",
    9376: "(e)",
    9377: "(f)",
    9378: "(g)",
    9379: "(h)",
    9380: "(i)",
    9381: "(j)",
    9382: "(k)",
    9383: "(l)",
    9384: "(m)",
    9385: "(n)",
    9386: "(o)",
    9387: "(p)",
    9388: "(q)",
    9389: "(r)",
    9390: "(s)",
    9391: "(t)",
    9392: "(u)",
    9393: "(v)",
    9394: "(w)",
    9395: "(x)",
    9396: "(y)",
    9397: "(z)",
    9398: "A",
    9399: "B",
    9400: "C",
    9401: "D",
    9402: "E",
    9403: "F",
    9404: "G",
    9405: "H",
    9406: "I",
    9407: "J",
    9408: "K",
    9409: "L",
    9410: "M",
    9411: "N",
    9412: "O",
    9413: "P",
    9414: "Q",
    9415: "R",
    9416: "S",
    9417: "T",
    9418: "U",
    9419: "V",
    9420: "W",
    9421: "X",
    9422: "Y",
    9423: "Z",
    9424: "a",
    9425: "b",
    9426: "c",
    9427: "d",
    9428: "e",
    9429: "f",
    9430: "g",
    9431: "h",
    9432: "i",
    9433: "j",
    9434: "k",
    9435: "l",
    9436: "m",
    9437: "n",
    9438: "o",
    9439: "p",
    9440: "q",
    9441: "r",
    9442: "s",
    9443: "t",
    9444: "u",
    9445: "v",
    9446: "w",
    9447: "x",
    9448: "y",
    9449: "z",
    9450: "0",
    9451: "11",
    9452: "12",
    9453: "13",
    9454: "14",
    9455: "15",
    9456: "16",
    9457: "17",
    9458: "18",
    9459: "19",
    9460: "20",
    9461: "1",
    9462: "2",
    9463: "3",
    9464: "4",
    9465: "5",
    9466: "6",
    9467: "7",
    9468: "8",
    9469: "9",
    9470: "10",
    9471: "0",
    10075: "'",
    10076: "'",
    10077: '"',
    10078: '"',
    10088: "(",
    10089: ")",
    10090: "(",
    10091: ")",
    10092: "<",
    10093: ">",
    10094: '"',
    10095: '"',
    10096: "<",
    10097: ">",
    10098: "[",
    10099: "]",
    10100: "{",
    10101: "}",
    10102: "1",
    10103: "2",
    10104: "3",
    10105: "4",
    10106: "5",
    10107: "6",
    10108: "7",
    10109: "8",
    10110: "9",
    10111: "10",
    10112: "1",
    10113: "2",
    10114: "3",
    10115: "4",
    10116: "5",
    10117: "6",
    10118: "7",
    10119: "8",
    10120: "9",
    10121: "10",
    10122: "1",
    10123: "2",
    10124: "3",
    10125: "4",
    10126: "5",
    10127: "6",
    10128: "7",
    10129: "8",
    10130: "9",
    10131: "10",
    11360: "L",
    11361: "l",
    11362: "L",
    11363: "P",
    11364: "R",
    11365: "a",
    11366: "t",
    11367: "H",
    11368: "h",
    11369: "K",
    11370: "k",
    11371: "Z",
    11372: "z",
    11374: "M",
    11375: "a",
    11377: "v",
    11378: "W",
    11379: "w",
    11380: "v",
    11381: "H",
    11382: "h",
    11384: "e",
    11386: "o",
    11387: "E",
    11388: "j",
    11816: "((",
    11817: "))",
    42792: "TZ",
    42793: "tz",
    42800: "F",
    42801: "S",
    42802: "AA",
    42803: "aa",
    42804: "AO",
    42805: "ao",
    42806: "AU",
    42807: "au",
    42808: "AV",
    42809: "av",
    42810: "AV",
    42811: "av",
    42812: "AY",
    42813: "ay",
    42814: "c",
    42815: "c",
    42816: "K",
    42817: "k",
    42818: "K",
    42819: "k",
    42820: "K",
    42821: "k",
    42822: "L",
    42823: "l",
    42824: "L",
    42825: "l",
    42826: "O",
    42827: "o",
    42828: "O",
    42829: "o",
    42830: "OO",
    42831: "oo",
    42832: "P",
    42833: "p",
    42834: "P",
    42835: "p",
    42836: "P",
    42837: "p",
    42838: "Q",
    42839: "q",
    42840: "Q",
    42841: "q",
    42842: "R",
    42843: "r",
    42846: "V",
    42847: "v",
    42848: "VY",
    42849: "vy",
    42850: "Z",
    42851: "z",
    42854: "TH",
    42855: "th",
    42856: "V",
    42873: "D",
    42874: "d",
    42875: "F",
    42876: "f",
    42877: "G",
    42878: "G",
    42879: "g",
    42880: "L",
    42881: "l",
    42882: "R",
    42883: "r",
    42884: "s",
    42885: "S",
    42886: "T",
    43003: "F",
    43004: "p",
    43005: "M",
    43006: "I",
    43007: "M",
    64256: "ff",
    64257: "fi",
    64258: "fl",
    64259: "ffi",
    64260: "ffl",
    64262: "st",
    65281: "!",
    65282: '"',
    65283: "#",
    65284: "$",
    65285: "%",
    65286: "&",
    65287: "'",
    65288: "(",
    65289: ")",
    65290: "*",
    65291: "+",
    65292: ",",
    65293: "-",
    65294: ".",
    65295: "/",
    65296: "0",
    65297: "1",
    65298: "2",
    65299: "3",
    65300: "4",
    65301: "5",
    65302: "6",
    65303: "7",
    65304: "8",
    65305: "9",
    65306: ":",
    65307: ";",
    65308: "<",
    65309: "=",
    65310: ">",
    65311: "?",
    65312: "@",
    65313: "A",
    65314: "B",
    65315: "C",
    65316: "D",
    65317: "E",
    65318: "F",
    65319: "G",
    65320: "H",
    65321: "I",
    65322: "J",
    65323: "K",
    65324: "L",
    65325: "M",
    65326: "N",
    65327: "O",
    65328: "P",
    65329: "Q",
    65330: "R",
    65331: "S",
    65332: "T",
    65333: "U",
    65334: "V",
    65335: "W",
    65336: "X",
    65337: "Y",
    65338: "Z",
    65339: "[",
    65340: "\\",
    65341: "]",
    65342: "^",
    65343: "_",
    65345: "a",
    65346: "b",
    65347: "c",
    65348: "d",
    65349: "e",
    65350: "f",
    65351: "g",
    65352: "h",
    65353: "i",
    65354: "j",
    65355: "k",
    65356: "l",
    65357: "m",
    65358: "n",
    65359: "o",
    65360: "p",
    65361: "q",
    65362: "r",
    65363: "s",
    65364: "t",
    65365: "u",
    65366: "v",
    65367: "w",
    65368: "x",
    65369: "y",
    65370: "z",
    65371: "{",
    65373: "}",
    65374: "~",
}


def normalize(string):
    """
    Normalize a string through possible permutations for comparison.

    View https://www.unicode.org/reports/tr44/#GC_Values_Table for General Category values.
    """
    if not string:
        return ""

    for char in string:
        # Remove Unicode control characters.
        # "C" is returned as the first char for all control chars.
        if unicodedata.category(char)[0] == "C":
            string = string.replace(char, "")

        # Normalize space separators into a single normal space
        if unicodedata.category(char) == "Zs":
            string = string.replace(char, " ")

    translate_table = string.maketrans(UNICODE)

    return string.translate(translate_table).strip().casefold()
