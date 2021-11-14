from src.broker.binance_.schema import (
    OPEN_TIME,
    HIGH_PRICE,
    LOW_PRICE,
    VOLUME,
    OPEN_PRICE,
    CLOSE_TIME,
)
from src.broker.binance_.transform import (
    transform_binance_historical_candles,
    transform_binance_stream_candle,
)

binance_historical_sample_data = [
    [
        1636151460000,
        "61182.64",
        "61208.15",
        "61182.63",
        "61197.05",
        "46.884",
        1636151519999,
        "2869268.92462",
        589,
        "21.380",
        "1308428.66129",
        "0",
    ],
    [
        1636151520000,
        "61197.05",
        "61201.54",
        "61132.27",
        "61158.16",
        "101.839",
        1636151579999,
        "6228134.89976",
        1156,
        "20.448",
        "1250882.28309",
        "0",
    ],
    [
        1636151580000,
        "61158.15",
        "61158.16",
        "61132.27",
        "61138.80",
        "35.364",
        1636151639999,
        "2162107.89368",
        735,
        "17.863",
        "1092110.11872",
        "0",
    ],
    [
        1636151640000,
        "61138.80",
        "61140.00",
        "61132.39",
        "61132.40",
        "29.484",
        1636151699999,
        "1802487.74411",
        570,
        "12.061",
        "737336.26644",
        "0",
    ],
    [
        1636151700000,
        "61132.40",
        "61153.57",
        "61132.27",
        "61132.28",
        "42.850",
        1636151759999,
        "2619766.13896",
        684,
        "27.468",
        "1679339.66770",
        "0",
    ],
    [
        1636151760000,
        "61132.27",
        "61145.97",
        "61090.00",
        "61097.73",
        "66.876",
        1636151819999,
        "4088021.94205",
        951,
        "18.046",
        "1103074.60671",
        "0",
    ],
    [
        1636151820000,
        "61097.24",
        "61111.23",
        "61069.41",
        "61097.98",
        "77.755",
        1636151879999,
        "4750046.97626",
        1184,
        "42.000",
        "2565757.42854",
        "0",
    ],
    [
        1636151880000,
        "61097.98",
        "61103.47",
        "61081.45",
        "61100.04",
        "40.070",
        1636151939999,
        "2447928.73395",
        665,
        "22.434",
        "1370555.50390",
        "0",
    ],
    [
        1636151940000,
        "61100.03",
        "61149.27",
        "61093.06",
        "61145.41",
        "100.813",
        1636151999999,
        "6162004.36648",
        939,
        "76.268",
        "4661674.62104",
        "0",
    ],
    [
        1636152000000,
        "61145.87",
        "61149.29",
        "61114.03",
        "61131.73",
        "38.427",
        1636152059999,
        "2349005.72923",
        603,
        "16.441",
        "1005023.16497",
        "0",
    ],
    [
        1636152060000,
        "61131.74",
        "61140.59",
        "61102.44",
        "61114.96",
        "43.696",
        1636152119999,
        "2670452.21255",
        639,
        "17.322",
        "1058632.18132",
        "0",
    ],
    [
        1636152120000,
        "61114.96",
        "61120.05",
        "61103.61",
        "61114.48",
        "22.315",
        1636152179999,
        "1363748.54483",
        433,
        "9.134",
        "558216.42195",
        "0",
    ],
    [
        1636152180000,
        "61114.49",
        "61120.00",
        "61107.82",
        "61107.82",
        "24.348",
        1636152239999,
        "1488047.43523",
        441,
        "6.065",
        "370668.57697",
        "0",
    ],
    [
        1636152240000,
        "61107.82",
        "61119.47",
        "61102.38",
        "61119.46",
        "22.611",
        1636152299999,
        "1381801.12049",
        416,
        "9.651",
        "589804.88472",
        "0",
    ],
    [
        1636152300000,
        "61119.47",
        "61129.13",
        "61106.20",
        "61127.69",
        "37.038",
        1636152359999,
        "2263725.70306",
        584,
        "18.084",
        "1105279.88990",
        "0",
    ],
    [
        1636152360000,
        "61127.69",
        "61131.59",
        "61120.01",
        "61127.22",
        "35.963",
        1636152419999,
        "2198294.90896",
        521,
        "20.246",
        "1237578.24839",
        "0",
    ],
    [
        1636152420000,
        "61127.21",
        "61184.18",
        "61127.21",
        "61180.10",
        "57.729",
        1636152479999,
        "3531045.99764",
        719,
        "50.142",
        "3066951.89560",
        "0",
    ],
    [
        1636152480000,
        "61180.10",
        "61184.19",
        "61153.29",
        "61176.02",
        "42.598",
        1636152539999,
        "2605833.23844",
        643,
        "26.205",
        "1603055.68744",
        "0",
    ],
    [
        1636152540000,
        "61176.03",
        "61187.76",
        "61162.86",
        "61177.13",
        "42.973",
        1636152599999,
        "2628936.90461",
        726,
        "15.011",
        "918326.94699",
        "0",
    ],
    [
        1636152600000,
        "61177.13",
        "61188.17",
        "61170.00",
        "61183.28",
        "36.619",
        1636152659999,
        "2240401.56495",
        598,
        "23.040",
        "1409643.63171",
        "0",
    ],
]

binance_stream_sample_data = {
    "e": "kline",
    "E": 1636237775563,
    "s": "BTCUSDT",
    "k": {
        "t": 1636236900000,
        "T": 1636237799999,
        "s": "BTCUSDT",
        "i": "15m",
        "f": 1132557641,
        "L": 1132564219,
        "o": "61475.78000000",
        "c": "61322.48000000",
        "h": "61489.63000000",
        "l": "61310.32000000",
        "v": "127.03730000",
        "n": 6579,
        "x": False,
        "q": "7798213.03210950",
        "V": "56.09761000",
        "Q": "3443652.98005460",
        "B": "0",
    },
}


def test_binance_lists_to_dataframe():
    df = transform_binance_historical_candles(
        binance_historical_sample_data,
        [OPEN_TIME, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, VOLUME],
    )

    columns = df.columns
    assert OPEN_TIME in columns
    assert VOLUME in columns
    assert CLOSE_TIME not in columns
    assert len(columns) == 5

    assert df.shape == (20, 5)

    assert df[OPEN_TIME][0] == 1636151460


def test_append_streaming_data():
    historical_df = transform_binance_historical_candles(
        binance_historical_sample_data,
        [OPEN_TIME, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, VOLUME],
    )

    candle_df = transform_binance_stream_candle(
        binance_stream_sample_data["k"],
        [OPEN_TIME, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, VOLUME],
    )

    appended_df = historical_df.append(candle_df)

    assert appended_df.shape == (21, 5)