from collections import Counter
from espn_api.basketball import League
from collect_data import fetch_all_player, save_historical_data

# Replace with my details
league_id = 1937531242  # my league ID
season_year = 2025  # Current season year
swid = "{B3AC659D-1A6F-4431-8A6B-45355773BA9C}"
espn_s2 = ("AEBXZygTTQ9lwpUMTjrlaqi70u8ao47ec7vHdc2RdJOJewjYfOorUs6N4"
           "20yeu%2BXAZWkDn96Kn7EQUYvOcw%2B%2FIZ17%2BX38ERVTllLHhS5g%"
           "2FYTyMrEPRUAdp99PkVDcG0naoFyXgR42uPR3Ijqsstn7NmDeWnvFxQ%2"
           "FVmN%2FkbPOOw8M2Wh9Po9pWAx88uBDYWAbs1BC%2BpTLmFRbhVr%2Fucv2"
           "qQrPB9Lwp5ofYomhG49sv%2FIXQ7elCmhdR9ISk7uYtKbtewNwjFNLPGAhHK"
           "CKmeG%2Fu63xXa91ylmdR%2Fp54PhV68pJJg%3D%3D")  # my ESPN_S2 token

# Connecting to my league
league = League(league_id=league_id, year=season_year, swid=swid, espn_s2=espn_s2)

fetch_all_player(league)
save_historical_data(league, total_weeks=10)