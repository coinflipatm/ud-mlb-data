# PRE-DRAFT SHEET 2026-08-29  (built from boxscores through 2026-08-28, pitcher_logs through 2026-08-28)
League baselines (source: ud-mlb-data boxscores): bat-start mean 7.36, P20 0.072; team-game mean runs 4.46. Arm buckets by shrunk HR/9 terciles [1.04, 1.3] -> P20 index {'LOW_HR': 0.743, 'MID_HR': 0.993, 'HIGH_HR': 1.259} (n {'LOW_HR': 11965, 'MID_HR': 12467, 'HIGH_HR': 12272}).

## PITCHERS  (legal = win prob >= .50, not Coors, probable listed)  legal arms: 16 vs 6 drafters  -> abundant: arm waits (R3-R4)
           pitcher team opp home  win_prob            wp_src    k9  k9_shr  kbb  hr9  era  gs26  ip_per_gs  ud_mean  ud_p20  ud_max  ud_min  ud_n  spot_starter  coors  legal
Cristopher Sánchez  PHI LAA    A     0.665 MODEL(p_home_ens) 10.37    9.98 5.11 0.75 2.62    27       6.23    14.79   0.259   27.00   -4.67    27         False  False   True
      Cade Cavalli  WSH MIA    H     0.518 MODEL(p_home_ens) 10.23    9.83 3.93 1.03 3.21    28       5.31    12.02   0.107   25.00   -0.67    28         False  False   True
      Nolan McLean  NYM HOU    H     0.537 MODEL(p_home_ens) 10.17    9.78 2.90 0.91 3.21    26       5.72    12.54   0.074   21.00    2.33    27         False  False   True
       Blake Snell  LAD DET    A     0.554 MODEL(p_home_ens) 11.14    9.31 2.89 0.00 2.57     4       5.25    13.50   0.000   18.00    4.00     4         False  False   True
     Kevin Gausman  CHC CIN    H     0.665 MODEL(p_home_ens)  8.92    8.80 3.63 1.08 4.37    27       5.57    10.35   0.000   19.00   -2.00    27         False  False   True
      José Soriano  TOR SEA    H     0.552 MODEL(p_home_ens)  8.92    8.79 2.20 0.81 3.43    26       5.55    10.74   0.077   22.00    2.00    26         False  False   True
      Shane Drohan  MIL TEX    H     0.663 MODEL(p_home_ens)  8.89    8.74 2.89 0.77 3.84    15       7.02     9.24   0.000   17.00    1.67    15         False  False   True
         Max Fried  NYY BOS    H     0.515 MODEL(p_home_ens)  8.24    8.27 2.93 0.21 2.81    15       5.76    11.21   0.062   22.00    2.00    16         False  False   True
        Kyle Leahy  STL PIT    H     0.528 MODEL(p_home_ens)  8.19    8.23 3.11 0.85 3.13    25       5.05     9.41   0.000   16.00    2.00    25         False  False   True
    Foster Griffin  CLE  KC    H     0.562 MODEL(p_home_ens)  8.14    8.18 3.55 1.39 3.19    26       5.74    11.55   0.115   20.33    2.33    26         False  False   True
         Shane Baz  BAL ATH    A     0.562 MODEL(p_home_ens)  8.03    8.10 2.60 0.65 4.04    26       5.82     9.97   0.038   20.00    0.00    26         False  False   True
    Matt Wilkinson   SF  AZ    H     0.517 MODEL(p_home_ens)  3.18    7.71 2.00 1.59 6.35     2       2.83     1.84   0.000    2.00    1.67     2          True  False   True
      Jake Bennett  BOS NYY    A     0.511 MODEL(p_home_ens)  6.88    7.34 3.72 0.72 3.49    15       5.84    10.61   0.000   18.00    2.33    17         False  False   True
      Martín Pérez  ATL COL    H     0.685 MODEL(p_home_ens)  6.63    7.08 1.77 0.94 3.12    21       5.49     8.10   0.000   18.00    1.33    21         False  False   True
       Erick Fedde  CWS MIN    A     0.504 MODEL(p_home_ens)  6.39    6.88 1.95 1.67 4.18    12       9.86     6.72   0.000   14.00    1.00    12         False  False   True
     Nick Martinez   TB  SD    H     0.524 MODEL(p_home_ens)  5.30    5.95 3.95 1.04 2.93    25       5.91     9.95   0.000   18.00   -1.00    25         False  False   True
      Jack Perkins  ATH BAL    H     0.438 MODEL(p_home_ens) 10.36    9.74 2.74 1.69 6.68    11       8.21     5.79   0.000    9.00    1.00    11         False  False  False
      Carlos Rodón  NYY BOS    H     0.489 MODEL(p_home_ens)  9.61    9.07 1.93 0.66 3.15    11       4.94    10.03   0.000   15.00    5.00    11         False  False  False
       Lake Bachar  PIT STL    A     0.472 MODEL(p_home_ens)  9.25    8.93 2.50 1.48 3.70     6      12.17     4.50   0.000    7.00    1.33     6         False  False  False
     Bennett Sousa  HOU NYM    A     0.463 MODEL(p_home_ens) 10.13    8.92 2.10 0.96 6.27     0      18.67      NaN     NaN     NaN     NaN     0          True  False  False
     Kade Anderson  SEA TOR    A     0.448 MODEL(p_home_ens)  7.94    8.30 2.50 3.18 4.76     1       5.67     7.67   0.000    7.67    7.67     1          True  False  False
    Walker Buehler   SD  TB    A     0.476 MODEL(p_home_ens)  7.69    7.85 2.20 1.07 4.63    26       4.86     7.82   0.000   15.00   -1.00    26         False  False  False
       Alec Gamboa  BOS NYY    A     0.485 MODEL(p_home_ens)  6.10    7.58 2.33 0.44 1.31     1      20.67     2.33   0.000    2.33    2.33     1          True  False  False
       Mitch Bratt   AZ  SF    A     0.490 MODEL(p_home_ens)  6.35    7.36 1.12 1.13 4.54     9       4.41     6.19   0.111   21.00    0.00     9         False  False  False
     Andrew Abbott  CIN CHC    A     0.335 MODEL(p_home_ens)  7.06    7.34 1.68 1.11 4.15    27       5.38     8.79   0.000   16.00   -3.00    27         False  False  False
   Daniel Lynch IV   KC CLE    A     0.438 MODEL(p_home_ens)  6.63    7.33 2.53 0.62 2.93     4      14.58     2.83   0.000    4.33    0.67     4         False  False  False
      Ryan Johnson  LAA PHI    H     0.335 MODEL(p_home_ens)  6.68    7.30 1.61 2.14 5.75    13       5.18     6.64   0.000   19.00   -0.67    13         False  False  False
     Cal Quantrill  TEX MIL    A     0.337 MODEL(p_home_ens)  6.45    7.07 2.73 0.97 2.90    10       8.37     9.53   0.000   17.00    1.00    10         False  False  False
   Sandy Alcantara  MIA WSH    A     0.482 MODEL(p_home_ens)  6.71    7.01 2.80 0.88 3.38    28       6.56    12.17   0.107   21.00    1.67    28         False  False  False
        Zach Agnos  COL ATL    A     0.315 MODEL(p_home_ens)  6.04    6.84 1.96 1.07 5.68     2      38.00     5.50   0.000    9.00    2.00     2          True  False  False
       Bailey Ober  MIN CWS    H     0.496 MODEL(p_home_ens)  6.15    6.74 2.55 1.50 4.49    20       5.42     8.02   0.050   21.00    0.67    20         False  False  False
    Keider Montero  DET LAD    H     0.446 MODEL(p_home_ens)  5.99    6.54 2.97 0.94 3.30    21       6.37     8.97   0.000   18.00    1.33    21         False  False  False
     Merrill Kelly   AZ  SF    A     0.483 MODEL(p_home_ens)  5.88    6.45 1.47 1.74 5.35    24       5.61     7.49   0.000   17.00    0.00    24         False  False  False
               NaN   SF  AZ    H     0.510 MODEL(p_home_ens)   NaN     NaN  NaN  NaN  NaN     0        NaN      NaN     NaN     NaN     NaN     0          True  False  False

## TEAMS  (sorted tier-first, then stack_score = run_est x park*arm mult x spot bump; tier per Rule 16; tier_adj = spot-starter bump)
team opp home venue  implied  total  win_prob               src tier tier_adj             opp_sp  opp_k9  opp_hr9  opp_gs26  spot_starter arm_bucket  park_runs_idx  park_p20_idx  arm_idx  mult  split_n  split_mean  split_p5  split_p9  split_p12  l15_mean  stack_score  lineup_posted
 BAL ATH    A   ATH      NaN    NaN     0.562 MODEL(p_home_ens)    ?        ?       Jack Perkins   10.36     1.69        11         False    HIGH_HR          1.235         1.391    1.259 1.751       67        4.64     0.463     0.104      0.045      4.80         8.12           True
 CWS MIN    A   MIN      NaN    NaN     0.504 MODEL(p_home_ens)    ?        ?        Bailey Ober    6.15     1.50        20         False    HIGH_HR          1.008         0.994    1.259 1.251       66        4.68     0.485     0.152      0.015      5.13         5.85           True
 CHC CIN    H   CHC      NaN    NaN     0.665 MODEL(p_home_ens)    ?        ?      Andrew Abbott    7.06     1.11        27         False     MID_HR          1.038         1.138    0.993 1.130       67        4.99     0.493     0.119      0.045      5.40         5.64           True
 MIN CWS    H   MIN      NaN    NaN     0.496 MODEL(p_home_ens)    ?        ?        Erick Fedde    6.39     1.67        12         False    HIGH_HR          1.008         0.994    1.259 1.251       67        4.46     0.433     0.134      0.015      4.13         5.58           True
 MIA WSH    A   WSH      NaN    NaN     0.482 MODEL(p_home_ens)    ?        ?       Cade Cavalli   10.23     1.03        28         False     MID_HR          1.166         1.257    0.993 1.248       66        4.32     0.394     0.136      0.045      3.73         5.39           True
 WSH MIA    H   WSH      NaN    NaN     0.518 MODEL(p_home_ens)    ?        ?    Sandy Alcantara    6.71     0.88        28         False     LOW_HR          1.166         1.257    0.743 0.934       67        5.52     0.582     0.194      0.060      4.20         5.16           True
 ATH BAL    H   ATH      NaN    NaN     0.438 MODEL(p_home_ens)    ?        ?          Shane Baz    8.03     0.65        26         False     LOW_HR          1.235         1.391    0.743 1.034       66        4.97     0.500     0.106      0.061      4.33         5.14           True
 MIL TEX    H   MIL      NaN    NaN     0.663 MODEL(p_home_ens)    ?        ?      Cal Quantrill    6.45     0.97        10         False     MID_HR          0.979         0.918    0.993 0.912       70        5.27     0.500     0.129      0.071      5.27         4.81           True
 CIN CHC    A   CHC      NaN    NaN     0.335 MODEL(p_home_ens)    ?        ?      Kevin Gausman    8.92     1.08        27         False     MID_HR          1.038         1.138    0.993 1.130       67        4.16     0.388     0.119      0.015      3.67         4.70           True
 ATL COL    H   ATL      NaN    NaN     0.685 MODEL(p_home_ens)    ?        ?         Zach Agnos    6.04     1.07         2          True     MID_HR          0.985         0.896    0.993 0.890       69        4.90     0.536     0.087      0.043      2.93         4.67           True
  SF  AZ    H    SF      NaN    NaN     0.517 MODEL(p_home_ens)    ?        ?      Merrill Kelly    5.88     1.74        24         False    HIGH_HR          0.964         0.859    1.259 1.081       67        4.12     0.403     0.075      0.015      3.80         4.45           True
  TB  SD    H    TB      NaN    NaN     0.524 MODEL(p_home_ens)    ?        ?     Walker Buehler    7.69     1.07        26         False     MID_HR          0.984         0.987    0.993 0.980       67        4.54     0.507     0.075      0.030      4.20         4.45           True
  SD  TB    A    TB      NaN    NaN     0.476 MODEL(p_home_ens)    ?        ?      Nick Martinez    5.30     1.04        25         False     MID_HR          0.984         0.987    0.993 0.980       66        4.52     0.470     0.076      0.015      4.33         4.43           True
 TOR SEA    H   TOR      NaN    NaN     0.552 MODEL(p_home_ens)    ?        ?      Kade Anderson    7.94     3.18         1          True    HIGH_HR          0.954         0.834    1.259 1.050       69        3.84     0.362     0.043      0.014      4.20         4.31           True
  KC CLE    A   CLE      NaN    NaN     0.438 MODEL(p_home_ens)    ?        ?     Foster Griffin    8.14     1.39        26         False    HIGH_HR          0.953         0.890    1.259 1.121       69        3.72     0.275     0.072      0.043      5.60         4.17           True
 NYM HOU    H   NYM      NaN    NaN     0.537 MODEL(p_home_ens)    ?        ?      Bennett Sousa   10.13     0.96         0          True     MID_HR          0.964         0.978    0.993 0.971       71        3.99     0.324     0.113      0.028      3.53         4.15           True
 STL PIT    H   STL      NaN    NaN     0.528 MODEL(p_home_ens)    ?        ?        Lake Bachar    9.25     1.48         6         False    HIGH_HR          0.954         0.855    1.259 1.076       71        3.80     0.352     0.056      0.000      5.00         4.09           True
  AZ  SF    A    SF      NaN    NaN     0.483 MODEL(p_home_ens)    ?        ?     Matt Wilkinson    3.18     1.59         2          True     MID_HR          0.964         0.859    0.993 0.853       68        4.46     0.426     0.132      0.015      4.53         4.07           True
  AZ  SF    A    SF      NaN    NaN     0.490 MODEL(p_home_ens)    ?        ?                NaN     NaN      NaN         0          True     MID_HR          0.964         0.859    0.993 0.853       68        4.46     0.426     0.132      0.015      4.53         4.07          False
 PHI LAA    A   LAA      NaN    NaN     0.665 MODEL(p_home_ens)    ?        ?       Ryan Johnson    6.68     2.14        13         False    HIGH_HR          0.914         0.795    1.259 1.001       67        4.06     0.433     0.090      0.015      5.27         4.06          False
 NYY BOS    H   NYY      NaN    NaN     0.515 MODEL(p_home_ens)    ?        ?        Alec Gamboa    6.10     0.44         1          True     LOW_HR          0.973         1.053    0.743 0.782       66        4.45     0.409     0.152      0.045      3.80         3.72           True
 BOS NYY    A   NYY      NaN    NaN     0.511 MODEL(p_home_ens)    ?        ?       Carlos Rodón    9.61     0.66        11         False     LOW_HR          0.973         1.053    0.743 0.782       67        4.51     0.448     0.104      0.015      5.07         3.53           True
 BOS NYY    A   NYY      NaN    NaN     0.485 MODEL(p_home_ens)    ?        ?          Max Fried    8.24     0.21        15         False     LOW_HR          0.973         1.053    0.743 0.782       67        4.51     0.448     0.104      0.015      5.07         3.53           True
  SF  AZ    H    SF      NaN    NaN     0.510 MODEL(p_home_ens)    ?        ?        Mitch Bratt    6.35     1.13         9         False     MID_HR          0.964         0.859    0.993 0.853       67        4.12     0.403     0.075      0.015      3.80         3.51          False
 HOU NYM    A   NYM      NaN    NaN     0.463 MODEL(p_home_ens)    ?        ?       Nolan McLean   10.17     0.91        26         False     LOW_HR          0.964         0.978    0.743 0.727       67        4.81     0.478     0.194      0.000      4.20         3.50           True
 NYY BOS    H   NYY      NaN    NaN     0.489 MODEL(p_home_ens)    ?        ?       Jake Bennett    6.88     0.72        15         False     LOW_HR          0.973         1.053    0.743 0.782       66        4.45     0.409     0.152      0.045      3.80         3.48           True
 LAD DET    A   DET      NaN    NaN     0.554 MODEL(p_home_ens)    ?        ?     Keider Montero    5.99     0.94        21         False     LOW_HR          0.937         0.835    0.743 0.620       69        5.51     0.493     0.217      0.116      4.07         3.42           True
 COL ATL    A   ATL      NaN    NaN     0.315 MODEL(p_home_ens)    ?        ?       Martín Pérez    6.63     0.94        21         False     LOW_HR          0.985         0.896    0.743 0.666       70        4.34     0.329     0.100      0.057      4.00         2.89           True
 TEX MIL    A   MIL      NaN    NaN     0.337 MODEL(p_home_ens)    ?        ?       Shane Drohan    8.89     0.77        15         False     LOW_HR          0.979         0.918    0.743 0.682       69        4.10     0.420     0.043      0.000      3.13         2.80           True
 PIT STL    A   STL      NaN    NaN     0.472 MODEL(p_home_ens)    ?        ?         Kyle Leahy    8.19     0.85        25         False     LOW_HR          0.954         0.855    0.743 0.635       72        4.33     0.431     0.097      0.042      3.73         2.75           True
 DET LAD    H   DET      NaN    NaN     0.446 MODEL(p_home_ens)    ?        ?        Blake Snell   11.14     0.00         4         False     LOW_HR          0.937         0.835    0.743 0.620       67        4.31     0.403     0.104      0.015      3.20         2.67           True
 CLE  KC    H   CLE      NaN    NaN     0.562 MODEL(p_home_ens)    ?        ?    Daniel Lynch IV    6.63     0.62         4         False     LOW_HR          0.953         0.890    0.743 0.661       68        4.01     0.397     0.059      0.015      4.20         2.65           True
 SEA TOR    A   TOR      NaN    NaN     0.448 MODEL(p_home_ens)    ?        ?       José Soriano    8.92     0.81        26         False     LOW_HR          0.954         0.834    0.743 0.620       67        3.99     0.358     0.104      0.015      4.27         2.47           True
 LAA PHI    H   LAA      NaN    NaN     0.335 MODEL(p_home_ens)    ?        ? Cristopher Sánchez   10.37     0.75        27         False     LOW_HR          0.914         0.795    0.743 0.591       69        3.57     0.319     0.043      0.000      4.20         2.11           True

## GAME A = BAL (game 824961)   GAME B = CWS (game 823665)   ACE = Cristopher Sánchez (PHI, wp 0.665 MODEL(p_home_ens), k9 10.37, ud_mean 14.79, max 27.0)
   Override A/B by hand if the market disagrees with the sheet — but do it BEFORE the lobby, never on the clock.

## BATS  (law_rank = Rule 8/16 order: tier, then stack_score, then slots 3-6 > B1-2 elite power > B1-2 > 7-9, then adj_mean.  model_rank = pure adj_mean, logged for open question 3)
   adj_mean = shrunk season mean UD x park*arm mult.  start_rate15 < 0.8 = sit risk (probability, not a fact).  starts < 40 = thin sample.
 law_rank  model_rank                       player team tier  slot pos    lineup_src  adj_mean  mean_ud  l15_mean   p20  adj_p20  max_ud  starts  modal_slot  start_rate15  zeros_rate  elite_power  blocked
        1           2 Christian Encarnacion-Strand  BAL    ?     4  3B        POSTED     14.11     9.07      8.93 0.214    0.375    29.0      28         6.0          0.87       0.250         True    False
        2           3             Gunnar Henderson  BAL    ?     3  SS        POSTED     13.76     8.01      9.00 0.081    0.142    32.0     135         3.0          0.93       0.200        False    False
        3           5               Samuel Basallo  BAL    ?     5   C        POSTED     12.57     7.09      3.47 0.074    0.130    32.0      81         5.0          0.40       0.358        False    False
        4           7                Dylan Beavers  BAL    ?     6  LF        POSTED     12.05     6.58      7.73 0.031    0.054    24.0      64         6.0          0.60       0.266        False    False
        5           1                  Pete Alonso  BAL    ?     2  DH        POSTED     15.79     9.51     12.47 0.131    0.229    43.0     137         2.0          1.00       0.131         True    False
        6           8             Jackson Holliday  BAL    ?     1  2B        POSTED     11.98     6.55      6.33 0.054    0.095    24.0      74         1.0          1.00       0.243        False    False
        7           4                    Coby Mayo  BAL    ?     7  1B        POSTED     12.64     7.16      9.27 0.043    0.075    25.0      94         4.0          0.87       0.277        False    False
        8           6                Leody Taveras  BAL    ?     9  RF        POSTED     12.24     6.84      6.27 0.059    0.103    23.0     101         9.0          0.87       0.228        False    False
        9          12                Colton Cowser  BAL    ?     8  CF        POSTED     11.28     5.97      7.53 0.051    0.089    28.0      79         8.0          0.47       0.304        False    False
       10           9                Miguel Vargas  CWS    ?     3  3B        POSTED     11.83    10.12     12.60 0.132    0.165    41.0     129         3.0          0.93       0.155         True    False
       11          23            Colson Montgomery  CWS    ?     6  SS        POSTED      9.83     8.02      6.40 0.104    0.130    32.0     125         6.0          0.93       0.264        False    False
       12          35            Braden Montgomery  CWS    ?     5  RF        POSTED      9.31     7.49      7.67 0.092    0.115    24.0      65         5.0          0.93       0.185        False    False
       13          44            Andrew Benintendi  CWS    ?     4  DH        POSTED      9.07     7.20      5.87 0.094    0.118    30.0      96         4.0          0.73       0.229        False    False
       14          11            Munetaka Murakami  CWS    ?     2  1B        POSTED     11.55    10.00      7.93 0.165    0.206    41.0      97         2.0          0.93       0.144         True    False
       15          20                Sam Antonacci  CWS    ?     1  LF        POSTED     10.12     8.38      8.13 0.069    0.086    30.0     101         1.0          0.93       0.198        False    False
       16          31               Chase Meidroth  CWS    ?     7  2B        POSTED      9.45     7.61      6.53 0.039    0.049    41.0     127         7.0          1.00       0.181        False    False
       17          43               Tristan Peters  CWS    ?     8  CF        POSTED      9.12     7.27     11.87 0.058    0.073    39.0     104         8.0          0.87       0.288        False    False
       18          91                  Jake Rogers  CWS    ?     9   C        POSTED      7.69     4.95      6.20 0.050    0.063    23.0      40         9.0          0.33       0.300        False    False
       19          33                 Alex Bregman  CHC    ?     3  3B        POSTED      9.42     8.64     11.13 0.090    0.102    56.0     133         4.0          1.00       0.135        False    False
       20          41                Michael Busch  CHC    ?     4  1B        POSTED      9.13     8.30      8.27 0.096    0.108    27.0     135         3.0          0.93       0.193        False    False
       21          55                 Nico Hoerner  CHC    ?     5  SS        POSTED      8.63     7.73      6.33 0.083    0.094    34.0     133         6.0          0.93       0.150        False    False
       22          56                    Matt Shaw  CHC    ?     6  RF        POSTED      8.63     7.97      8.73 0.091    0.103    28.0      33         7.0          0.00       0.273        False    False
       23          10          Pete Crow-Armstrong  CHC    ?     1  CF        POSTED     11.63    11.15     10.67 0.175    0.198    46.0     137         1.0          1.00       0.168         True    False
       24          15                 Seiya Suzuki  CHC    ?     2  DH        POSTED     10.33     9.77     11.07 0.139    0.157    34.0     115         2.0          1.00       0.183         True    False
       25          48                Pedro Ramírez  CHC    ?     8  2B        POSTED      8.97     8.54      9.53 0.154    0.174    32.0      39         7.0          0.93       0.231        False    False
       26          70                 Carson Kelly  CHC    ?     9   C        POSTED      8.20     7.22      6.73 0.060    0.068    37.0      83         9.0          0.60       0.205        False    False
       27          88                Tyrone Taylor  CHC    ?     7  LF        POSTED      7.75     6.43      9.20 0.065    0.073    28.0      46         9.0          0.33       0.239        False    False
       28          17                 Kody Clemens  MIN    ?     3  2B        POSTED     10.23     8.48      8.73 0.126    0.158    29.0     111         5.0          0.87       0.189         True    False
       29          22                    Josh Bell  MIN    ?     4  DH        POSTED      9.90     8.09      8.73 0.066    0.083    36.0     121         3.0          0.93       0.149        False    False
       30          30               Trevor Larnach  MIN    ?     6  LF        POSTED      9.46     7.65      5.00 0.098    0.123    26.0      92         1.0          0.60       0.228        False    False
       31          32                  Royce Lewis  MIN    ?     5  1B        POSTED      9.43     7.61      5.87 0.051    0.064    25.0      98         6.0          1.00       0.163        False    False
       32          27                   Brooks Lee  MIN    ?     2  3B        POSTED      9.61     7.78      9.07 0.073    0.091    30.0     124         7.0          1.00       0.234         True    False
       33          28               Luke Keaschall  MIN    ?     1  RF        POSTED      9.57     7.74      9.80 0.042    0.053    24.0     120         1.0          1.00       0.150        False    False
       34          37             Kaelen Culpepper  MIN    ?     7  SS        POSTED      9.17     7.25      6.80 0.000    0.000    16.0      16         9.0          0.93       0.062        False    False
       35          38               Walker Jenkins  MIN    ?     9  CF        POSTED      9.17     6.00      6.00 0.000    0.000     6.0       1         9.0          0.07       0.000        False    False
       36          64              Victor Caratini  MIN    ?     8   C        POSTED      8.31     6.29      4.13 0.061    0.076    27.0      82         8.0          0.40       0.207        False    False
       37          13                   Otto Lopez  MIA    ?     5  SS        POSTED     10.65     8.90      6.33 0.109    0.136    32.0     128         1.0          1.00       0.172        False    False
       38          25               Xavier Edwards  MIA    ?     3  2B        POSTED      9.73     7.94      6.80 0.046    0.057    25.0     130         4.0          1.00       0.115        False    False
       39          34               Griffin Conine  MIA    ?     4  DH        POSTED      9.32     7.56      8.93 0.140    0.175    33.0      50         4.0          0.80       0.240         True    False
       40          36                 Jakob Marsee  MIA    ?     6  CF        POSTED      9.26     7.43      8.87 0.070    0.087    29.0     115         1.0          0.73       0.183        False    False
       41          24          Heriberto Hernández  MIA    ?     2  LF        POSTED      9.81     8.10      9.93 0.098    0.122    40.0      82         2.0          0.93       0.183         True    False
       42          21                 Kyle Stowers  MIA    ?     1  1B        POSTED     10.12     8.44      9.40 0.096    0.120    43.0      94         6.0          0.13       0.202        False    False
       43          51                Javier Sanoja  MIA    ?     7  3B        POSTED      8.86     6.99      8.07 0.101    0.126    28.0      89         6.0          0.80       0.281        False    False
       44          58                 Owen Caissie  MIA    ?     8  RF        POSTED      8.56     6.63      5.00 0.072    0.090    27.0      83         7.0          0.60       0.337        False    False
       45          72                     Joe Mack  MIA    ?     9   C        POSTED      8.02     5.90      4.73 0.028    0.035    29.0      71         8.0          0.60       0.366        False    False
       46         103                  Daylen Lile  WSH    ?     4  RF        POSTED      7.56     8.31     10.67 0.118    0.110    38.0     127         4.0          1.00       0.213        False    False
       47         136                  Dylan Crews  WSH    ?     5  CF        POSTED      7.03     7.62      6.80 0.013    0.012    22.0      77         3.0          0.87       0.169        False    False
       48         141                 Keibert Ruiz  WSH    ?     6   C        POSTED      6.92     7.44      9.20 0.062    0.058    37.0      80         6.0          0.60       0.288        False    False
       49         193                    José Tena  WSH    ?     3  LF        POSTED      6.16     6.10      5.33 0.033    0.031    24.0      61         3.0          0.33       0.262        False    False
       50          42                    CJ Abrams  WSH    ?     1  DH        POSTED      9.13    10.54      8.27 0.167    0.156    36.0     126         1.0          0.73       0.159         True    False
       51         143               Abimelec Ortiz  WSH    ?     2  1B        POSTED      6.82     7.17      7.07 0.056    0.052    23.0      18         2.0          0.80       0.278         True    False
       52         145                  Brady House  WSH    ?     7  3B        POSTED      6.79     7.20      8.13 0.085    0.079    28.0      59         5.0          0.87       0.203        False    False
       53         184                  Nasim Nuñez  WSH    ?     9  SS        POSTED      6.27     6.49      3.40 0.026    0.024    34.0     115         8.0          0.80       0.226        False    False
       54         210                 Jorbit Vivas  WSH    ?     8  2B        POSTED      5.90     5.77      5.60 0.013    0.012    26.0      75         6.0          0.73       0.213        False    False
       55          59                   Zack Gelof  ATH    ?     3  2B        POSTED      8.50     8.67      7.93 0.092    0.095    28.0      76         3.0          1.00       0.158         True    False
       56          95              Lawrence Butler  ATH    ?     4  RF        POSTED      7.68     7.47     10.40 0.043    0.044    30.0      92         4.0          1.00       0.185        False    False
       57         106               Donovan Walton  ATH    ?     6  SS        POSTED      7.50     7.16      6.60 0.000    0.000    18.0      45         8.0          0.73       0.178        False    False
       58         157                  Tommy White  ATH    ?     5  3B        POSTED      6.59     5.21      5.93 0.000    0.000    19.0      34         5.0          0.87       0.324        False    False
       59         105                  Henry Bolte  ATH    ?     1  CF        POSTED      7.54     7.25      8.87 0.024    0.025    32.0      83         1.0          1.00       0.181        False    False
       60         144                  Jeff McNeil  ATH    ?     2  1B        POSTED      6.82     6.29      8.73 0.020    0.021    33.0      98         2.0          0.80       0.224        False    False
       61         118                Carlos Cortes  ATH    ?     8  LF        POSTED      7.28     6.86      6.00 0.068    0.070    32.0      74         6.0          0.80       0.216        False    False
       62         121                    Max Muncy  ATH    ?     7  DH        POSTED      7.20     6.69      5.73 0.034    0.035    29.0      59         7.0          0.73       0.186        False    False
       63         128                   Jonah Heim  ATH    ?     9   C        POSTED      7.14     6.66      4.67 0.082    0.085    30.0      73         4.0          0.67       0.260         True    False
       64          57                  Jake Bauers  MIL    ?     3  1B        POSTED      8.57    10.12     11.80 0.168    0.153    32.0     113         3.0          0.87       0.142         True    False
       65         112             Garrett Mitchell  MIL    ?     5  CF        POSTED      7.37     8.35      7.00 0.067    0.061    32.0     105         7.0          0.53       0.181        False    False
       66         117             Christian Yelich  MIL    ?     6  DH        POSTED      7.30     8.28      8.07 0.078    0.071    27.0      90         6.0          0.67       0.211        False    False
       67         122            William Contreras  MIL    ?     4   C        POSTED      7.20     8.07      9.60 0.100    0.091    39.0     120         3.0          0.93       0.192        False    False
       68          68              Jackson Chourio  MIL    ?     2  LF        POSTED      8.23     9.71      9.13 0.134    0.122    46.0      97         1.0          1.00       0.124         True    False
       69          71                 Brice Turang  MIL    ?     1  2B        POSTED      8.20     9.51      7.07 0.111    0.101    36.0     126         1.0          0.67       0.127        False    False
       70         146                 Cooper Pratt  MIL    ?     8  SS        POSTED      6.79     7.50      5.93 0.083    0.076    28.0      48         8.0          0.33       0.292        False    False
       71         147                    Luis Lara  MIL    ?     7  RF        POSTED      6.78     7.52      6.33 0.097    0.088    28.0      31         2.0          0.73       0.194        False    False
       72         180               David Hamilton  MIL    ?     9  3B        POSTED      6.34     6.76      8.60 0.034    0.031    36.0      88         9.0          0.60       0.330        False    False
       73          18                  Sal Stewart  CIN    ?     3  1B        POSTED     10.16     9.47      8.60 0.124    0.140    36.0     137         2.0          1.00       0.153         True    False
       74          46                    JJ Bleday  CIN    ?     4  LF        POSTED      9.02     8.22      6.40 0.105    0.119    39.0     105         3.0          0.93       0.229         True    False
       75          87             Tyler Stephenson  CIN    ?     5  DH        POSTED      7.82     6.73      7.00 0.062    0.070    36.0      97         4.0          0.73       0.268        False    False
       76          89               Eugenio Suárez  CIN    ?     6  3B        POSTED      7.72     6.62      6.40 0.096    0.108    36.0     104         5.0          0.93       0.260        False    False
       77          16              Elly De La Cruz  CIN    ?     2  SS        POSTED     10.28     9.68      7.93 0.118    0.133    43.0     119         1.0          1.00       0.185        False    False
       78          75             Héctor Rodríguez  CIN    ?     1  RF        POSTED      8.00     6.33      6.33 0.067    0.076    25.0      15         7.0          0.53       0.267        False    False
       79          79                  Matt McLain  CIN    ?     9  2B        POSTED      7.97     6.93      7.33 0.117    0.132    35.0     103         6.0          1.00       0.282        False    False
       80         129                 Jose Trevino  CIN    ?     7   C        POSTED      7.14     5.14      5.73 0.057    0.064    31.0      35         7.0          0.47       0.429        False    False
       81         166                    TJ Friedl  CIN    ?     8  CF        POSTED      6.53     4.76      1.87 0.016    0.018    25.0      62         8.0          0.20       0.339        False    False
       82          80                   Matt Olson  ATL    ?     3  1B        POSTED      7.97     9.42      6.67 0.124    0.110    37.0     137         3.0          1.00       0.190         True    False
       83         120            Michael Harris II  ATL    ?     5  CF        POSTED      7.22     8.35      8.47 0.089    0.079    32.0     123         4.0          1.00       0.154        False    False
       84         152                 Ozzie Albies  ATL    ?     6  2B        POSTED      6.70     7.58      4.67 0.066    0.059    35.0     136         6.0          1.00       0.184        False    False
       85         174               Mauricio Dubón  ATL    ?     4  SS        POSTED      6.43     7.17      4.93 0.048    0.043    28.0     126         6.0          0.87       0.183        False    False
       86         102                Drake Baldwin  ATL    ?     1   C        POSTED      7.60     8.96      7.67 0.080    0.071    43.0     113         1.0          1.00       0.168         True    False
       87         109             Ronald Acuña Jr.  ATL    ?     2  RF        POSTED      7.47     8.88      7.53 0.096    0.085    39.0      83         2.0          0.93       0.169        False    False
       88         185                Dominic Smith  ATL    ?     9  DH        POSTED      6.27     6.87      5.93 0.072    0.064    28.0      69         7.0          0.20       0.232        False    False
       89         190                 Austin Riley  ATL    ?     8  3B        POSTED      6.24     6.90      5.67 0.068    0.061    35.0     133         8.0          0.93       0.286        False    False
       90         237             Mike Yastrzemski  ATL    ?     7  LF        POSTED      5.33     5.38      3.20 0.045    0.040    28.0      88         7.0          0.73       0.250        False    False
       91          49              Junior Caminero   TB    ?     3  3B        POSTED      8.94     9.64      7.33 0.141    0.138    48.0     135         3.0          1.00       0.163         True    False
       92          62               Bryce Eldridge   SF    ?     3  DH        POSTED      8.41     7.98      9.33 0.092    0.099    35.0      87         4.0          0.80       0.126        False    False
       93          65                   Liam Hicks   TB    ?     4   C        POSTED      8.29     8.87      8.20 0.084    0.082    32.0     107         4.0          0.80       0.159         True    False
       94          67                 Jung Hoo Lee   SF    ?     4  RF        POSTED      8.24     7.71      5.47 0.076    0.082    37.0     119         6.0          0.80       0.277        False    False
       95          97                  Turner Hill   SF    ?     5  LF        POSTED      7.66     5.89      5.89 0.000    0.000    15.0       9         7.0          0.60       0.222        False    False
       96         107                 Jonny DeLuca   TB    ?     6  RF        POSTED      7.50     7.83      7.73 0.094    0.092    27.0      64         6.0          0.73       0.250        False    False
       97         134             Chandler Simpson   TB    ?     5  LF        POSTED      7.04     7.12      7.47 0.025    0.024    24.0     120         5.0          0.93       0.167        False    False
       98         162               Drew Cavanaugh   SF    ?     6   C        POSTED      6.58     4.40      4.27 0.000    0.000    16.0      30         8.0          0.60       0.433        False    False
       99          45                Rafael Devers   SF    ?     2  1B        POSTED      9.05     8.67     11.20 0.102    0.110    34.0     137         2.0          1.00       0.190        False    False
      100          63                   Yandy Díaz   TB    ?     1  DH        POSTED      8.37     8.91      8.53 0.077    0.075    34.0     130         1.0          1.00       0.146        False    False
      101          76              Jonathan Aranda   TB    ?     2  1B        POSTED      8.00     8.41      6.00 0.063    0.062    28.0     127         2.0          0.93       0.150        False    False
      102         113                 Drew Gilbert   SF    ?     1  CF        POSTED      7.37     6.56      9.47 0.037    0.040    30.0      82         1.0          0.67       0.220        False    False
      103          83                Shay Whitcomb   SF    ?     7  3B        POSTED      7.93     7.25      7.25 0.125    0.135    24.0       8         7.0          0.33       0.500         True    False
      104         111                  Nate Furman   SF    ?     8  2B        POSTED      7.38     1.50      1.50 0.000    0.000     3.0       4         6.0          0.20       0.500        False    False
      105         132               Cedric Mullins   TB    ?     8  CF        POSTED      7.06     7.14      7.33 0.038    0.037    31.0     106         7.0          0.80       0.226        False    False
      106         154              Richie Palacios   TB    ?     7  2B        POSTED      6.68     6.56      7.13 0.048    0.047    26.0      84         8.0          0.73       0.310        False    False
      107         171               Christian Koss   SF    ?     9  SS        POSTED      6.48     4.28      6.07 0.000    0.000    16.0      32         9.0          1.00       0.312        False    False
      108         173                 Taylor Walls   TB    ?     9  SS        POSTED      6.46     6.29      6.80 0.029    0.028    30.0     102         9.0          0.80       0.196        False    False
      109          74                    Ty France   SD    ?     4  1B        POSTED      8.01     8.52      7.27 0.097    0.095    40.0      93         4.0          1.00       0.194         True    False
      110          81              Jackson Merrill   SD    ?     5  CF        POSTED      7.96     8.35      8.27 0.085    0.083    42.0     130         5.0          1.00       0.269        False    False
      111         110                Manny Machado   SD    ?     3  3B        POSTED      7.47     7.70      6.00 0.098    0.096    34.0     132         3.0          1.00       0.227         True    False
      112         124               Luis Campusano   SD    ?     6   C        POSTED      7.19     7.33      7.67 0.116    0.114    29.0      43         6.0          0.47       0.209        False    False
      113          54           Fernando Tatis Jr.   SD    ?     1  RF        POSTED      8.71     9.36     11.60 0.123    0.121    42.0     130         1.0          0.93       0.138        False    False
      114         167             Jake Cronenworth   SD    ?     2  SS        POSTED      6.53     6.30      7.27 0.013    0.013    20.0      79         2.0          1.00       0.253        False    False
      115         137                Dustin Harris   SD    ?     9  LF        POSTED      6.99     6.56      5.80 0.000    0.000    18.0      16         9.0          0.13       0.188        False    False
      116         149                 Luis Rengifo   SD    ?     8  2B        POSTED      6.75     6.65      6.80 0.038    0.037    23.0      80         6.0          0.87       0.212        False    False
      117         158                 Gavin Sheets   SD    ?     7  DH        POSTED      6.59     6.47      4.80 0.068    0.067    44.0     103         7.0          0.53       0.262        False    False
      118          60              George Springer  TOR    ?     4  DH        POSTED      8.42     8.30      9.47 0.093    0.098    30.0      97         4.0          0.67       0.165        False    False
      119          69               Kazuma Okamoto  TOR    ?     5  3B        POSTED      8.23     7.99      8.93 0.125    0.131    35.0     128         6.0          0.93       0.234         True    False
      120          98        Vladimir Guerrero Jr.  TOR    ?     3  1B        POSTED      7.64     7.25      5.60 0.042    0.044    28.0     120         3.0          0.60       0.200        False    False
      121         114               Charles McAdoo  TOR    ?     6  2B        POSTED      7.36     6.26      6.20 0.053    0.056    22.0      19         1.0          0.73       0.211        False    False
      122          77               Alejandro Kirk  TOR    ?     2   C        POSTED      7.99     7.79     11.00 0.057    0.060    29.0      53         3.0          0.80       0.151        False    False
      123          82                Brett Bateman  TOR    ?     1  RF        POSTED      7.94     8.06      7.67 0.000    0.000    19.0      16         1.0          0.80       0.125        False    False
      124         104                  Daz Cameron  TOR    ?     8  LF        POSTED      7.55     5.80      5.80 0.000    0.000    19.0       5         7.0          0.33       0.400         True    False
      125         123                Ernie Clement  TOR    ?     7  SS        POSTED      7.20     6.71      5.40 0.024    0.025    32.0     127         6.0          0.87       0.173        False    False
      126         156                  Myles Straw  TOR    ?     9  CF        POSTED      6.62     5.58      6.47 0.017    0.018    24.0      59         9.0          0.67       0.322        False    False
      127          39               Jac Caglianone   KC    ?     3  RF        POSTED      9.17     8.46     14.60 0.103    0.115    44.0     117         3.0          0.80       0.205         True    False
      128          61                Tyler Tolbert   KC    ?     6  CF        POSTED      8.42     7.71      7.47 0.097    0.109    38.0      31         7.0          0.47       0.290        False    False
      129          96                  Nick Loftin   KC    ?     5  3B        POSTED      7.67     6.59      6.40 0.075    0.084    33.0      80         1.0          0.87       0.262        False    False
      130          99               Salvador Perez   KC    ?     4  1B        POSTED      7.63     6.63      6.87 0.071    0.080    26.0     126         4.0          0.93       0.270        False    False
      131          53                Carter Jensen   KC    ?     1  DH        POSTED      8.79     8.01      9.07 0.070    0.078    33.0     115         1.0          0.80       0.235         True    False
      132          14               Bobby Witt Jr.   KC    ?     2  SS        POSTED     10.36     9.88     12.40 0.120    0.135    40.0     117         2.0          1.00       0.111        False    False
      133          66                 Matthew Lugo   KC    ?     8  LF        POSTED      8.25      NaN       NaN   NaN      NaN     NaN       0         NaN          0.00         NaN        False    False
      134          92                   Luke Maile   KC    ?     9   C        POSTED      7.69     4.67      4.67 0.111    0.124    23.0       9         8.0          0.20       0.444        False    False
      135         100                Isaac Collins   KC    ?     7  2B        POSTED      7.61     6.58      4.93 0.027    0.030    29.0     110         6.0          0.73       0.227        False    False
      136          86                 Carson Benge  NYM    ?     4  RF        POSTED      7.88     8.36      8.93 0.087    0.084    37.0     126         4.0          1.00       0.175        False    False
      137         135                  Bo Bichette  NYM    ?     3  3B        POSTED      7.04     7.22     10.20 0.082    0.080    36.0     134         3.0          0.93       0.201        False    False
      138         142                  Jared Young  NYM    ?     5  1B        POSTED      6.89     6.94      7.80 0.015    0.015    21.0      68         5.0          0.80       0.221        False    False
      139         191                Marcus Semien  NYM    ?     6  2B        POSTED      6.24     6.11      4.27 0.061    0.059    32.0     114         7.0          0.87       0.307        False    False
      140          50                    Juan Soto  NYM    ?     2  DH        POSTED      8.89    10.00      9.47 0.151    0.147    31.0      86         2.0          0.00       0.128         True    False
      141         101             Francisco Lindor  NYM    ?     1  SS        POSTED      7.61     8.09      7.87 0.117    0.114    47.0      77         2.0          1.00       0.273         True    False
      142         127                   A.J. Ewing  NYM    ?     7  CF        POSTED      7.18     7.40      4.33 0.068    0.066    40.0      88         1.0          1.00       0.216        False    False
      143         163            Francisco Alvarez  NYM    ?     9   C        POSTED      6.58     6.52      4.80 0.078    0.076    31.0      90         9.0          0.73       0.244        False    False
      144         197                   Brett Baty  NYM    ?     8  LF        POSTED      6.08     5.85      5.00 0.037    0.036    26.0     108         7.0          0.60       0.296        False    False
      145          19                Jordan Walker  STL    ?     4  RF        POSTED     10.15    10.04     12.33 0.119    0.128    35.0     134         4.0          1.00       0.142         True    False
      146          26                Alec Burleson  STL    ?     3  1B        POSTED      9.63     9.44      9.93 0.115    0.124    48.0     131         3.0          0.93       0.183        False    False
      147         131                  José Fermín  STL    ?     6  2B        POSTED      7.09     6.13      7.27 0.030    0.032    28.0      67         8.0          0.67       0.284        False    False
      148         133                Nathan Church  STL    ?     5  CF        POSTED      7.05     6.21      6.73 0.051    0.055    32.0      98         6.0          0.67       0.265        False    False
      149          47                JJ Wetherholt  STL    ?     1  SS        POSTED      9.01     8.69      7.53 0.102    0.110    38.0     128         1.0          0.87       0.172        False    False
      150          52                 Iván Herrera  STL    ?     2  DH        POSTED      8.83     8.46      6.33 0.073    0.079    36.0     137         2.0          1.00       0.161        False    False
      151          78                  Joshua Báez  STL    ?     8  LF        POSTED      7.98     7.62      7.62 0.077    0.083    46.0      13         5.0          0.80       0.308         True    False
      152         138                 Nolan Gorman  STL    ?     7  3B        POSTED      6.98     5.88      3.20 0.000    0.000    19.0      57         7.0          0.13       0.228        False    False
      153         181                 Jimmy Crooks  STL    ?     9   C        POSTED      6.33     4.36      5.60 0.000    0.000    16.0      39         8.0          0.40       0.359        False    False
      154         115               Gabriel Moreno   AZ    ?     3   C        POSTED      7.34     9.10     10.40 0.078    0.067    23.0     102         3.0          0.93       0.137        False    False
      155         116               Gabriel Moreno   AZ    ?     3  DH MODAL(last10)      7.34     9.10     10.40 0.078    0.067    23.0     102         3.0          0.93       0.137        False    False
      156         150              Geraldo Perdomo   AZ    ?     4  SS        POSTED      6.74     8.06      7.47 0.053    0.045    27.0     131         4.0          1.00       0.145        False    False
      157         151              Geraldo Perdomo   AZ    ?     4  SS MODAL(last10)      6.74     8.06      7.47 0.053    0.045    27.0     131         4.0          1.00       0.145        False    False
      158         169                Nolan Arenado   AZ    ?     5  DH        POSTED      6.49     7.69      8.87 0.098    0.084    37.0     122         5.0          0.80       0.238         True    False
      159         170                Nolan Arenado   AZ    ?     5  3B MODAL(last10)      6.49     7.69      8.87 0.098    0.084    37.0     122         5.0          0.80       0.238         True    False
      160         178                     Tim Tawa   AZ    ?     6  1B        POSTED      6.35     7.52      8.40 0.129    0.110    30.0      62         6.0          1.00       0.194        False    False
      161         179                     Tim Tawa   AZ    ?     6  1B MODAL(last10)      6.35     7.52      8.40 0.129    0.110    30.0      62         6.0          1.00       0.194        False    False
      162          93               Corbin Carroll   AZ    ?     2  RF        POSTED      7.69     9.52     11.07 0.135    0.115    35.0     133         2.0          1.00       0.158        False    False
      163          94               Corbin Carroll   AZ    ?     2  RF MODAL(last10)      7.69     9.52     11.07 0.135    0.115    35.0     133         2.0          1.00       0.158        False    False
      164         186              Ildemaro Vargas   AZ    ?     1  2B        POSTED      6.27     7.35      5.13 0.063    0.054    38.0      95         1.0          0.87       0.168        False    False
      165         187              Ildemaro Vargas   AZ    ?     1  2B MODAL(last10)      6.27     7.35      5.13 0.063    0.054    38.0      95         1.0          0.87       0.168        False    False
      166         205                Lars Nootbaar   AZ    ?     1  LF MODAL(last10)      5.93     6.68      6.20 0.051    0.044    27.0      59         1.0          0.53       0.203        False    False
      167         176                Jordan Lawlar   AZ    ?     8  CF        POSTED      6.37     7.70      8.20 0.100    0.085    26.0      20         7.0          0.53       0.300        False    False
      168         177                Jordan Lawlar   AZ    ?     7  LF MODAL(last10)      6.37     7.70      8.20 0.100    0.085    26.0      20         7.0          0.53       0.300        False    False
      169         198               Jose Fernandez   AZ    ?     7  3B        POSTED      6.07     6.92      6.00 0.041    0.035    35.0      49         8.0          0.47       0.143        False    False
      170         199               Jose Fernandez   AZ    ?     8  3B MODAL(last10)      6.07     6.92      6.00 0.041    0.035    35.0      49         8.0          0.47       0.143        False    False
      171         221             Ryan Waldschmidt   AZ    ?     9  LF        POSTED      5.68     6.23      5.47 0.046    0.039    32.0      65         9.0          0.80       0.246        False    False
      172         222             Ryan Waldschmidt   AZ    ?     9  CF MODAL(last10)      5.68     6.23      5.47 0.046    0.039    32.0      65         9.0          0.80       0.246        False    False
      173          40                 Bryce Harper  PHI    ?     3  RF MODAL(last10)      9.14     9.66     10.73 0.104    0.104    38.0     135         3.0          1.00       0.170         True    False
      174          73                  Luis Arraez  PHI    ?     4  2B MODAL(last10)      8.02     8.21      7.00 0.047    0.047    32.0     127         4.0          0.93       0.134        False    False
      175          85                 Bryson Stott  PHI    ?     6  3B MODAL(last10)      7.89     8.05      7.00 0.057    0.057    37.0     123         6.0          0.93       0.203        False    False
      176         119                    Alec Bohm  PHI    ?     5  1B MODAL(last10)      7.27     7.23     11.40 0.103    0.103    38.0     126         5.0          0.93       0.198        False    False
      177          29               Kyle Schwarber  PHI    ?     1  DH MODAL(last10)      9.57    10.25      9.47 0.147    0.147    53.0     129         1.0          1.00       0.147         True    False
      178          84                  Trea Turner  PHI    ?     2  SS MODAL(last10)      7.90     8.05      4.87 0.062    0.062    40.0     130         2.0          0.93       0.200        False    False
      179          90                Brandon Marsh  PHI    ?     7  LF MODAL(last10)      7.72     7.83      6.20 0.084    0.084    36.0     119         7.0          0.80       0.193        False    False
      180         153                J.T. Realmuto  PHI    ?     8   C MODAL(last10)      6.70     6.42      5.80 0.051    0.051    33.0      98         8.0          0.87       0.286        False    False
      181         159              Justin Crawford  PHI    ?     9  CF MODAL(last10)      6.59     6.28      5.27 0.029    0.029    25.0     104         9.0          0.80       0.250        False    False
      182         148              Luis García Jr.  NYY    ?     4  1B        POSTED      6.77     9.18      8.27 0.137    0.107    42.0     102         4.0          0.87       0.265        False    False
      183         188            Jazz Chisholm Jr.  NYY    ?     5  2B        POSTED      6.26     8.22      7.87 0.076    0.059    34.0     119         7.0          0.87       0.235        False    False
      184         224           George Lombard Jr.  NYY    ?     6  SS        POSTED      5.64     6.90      5.87 0.050    0.039    22.0      20         6.0          1.00       0.200        False    False
      185         229                 Heliot Ramos  NYY    ?     3  RF        POSTED      5.50     6.89      4.53 0.067    0.052    44.0      89         3.0          0.73       0.247        False    False
      186         125                     Ben Rice  NYY    ?     2  DH        POSTED      7.19     9.77      8.33 0.185    0.145    39.0     124         2.0          1.00       0.226         True    False
      187         183                Trent Grisham  NYY    ?     1  CF        POSTED      6.29     8.31     10.67 0.136    0.106    40.0     103         1.0          1.00       0.243        False    False
      188         215                Spencer Jones  NYY    ?     7  LF        POSTED      5.72     7.28      8.87 0.100    0.078    26.0      50         5.0          0.93       0.300        False    False
      189         216               José Caballero  NYY    ?     9  3B        POSTED      5.72     7.30      7.27 0.040    0.031    32.0     100         9.0          0.60       0.220        False    False
      190         289                 Austin Wells  NYY    ?     8   C        POSTED      4.32     4.70      4.00 0.011    0.009    25.0      88         8.0          0.87       0.386        False    False
      191         139            Willson Contreras  BOS    ?     4  1B        POSTED      6.96     9.41      8.53 0.107    0.084    31.0     122         4.0          0.93       0.107         True    False
      192         140            Willson Contreras  BOS    ?     4  1B        POSTED      6.96     9.41      8.53 0.107    0.084    31.0     122         4.0          0.93       0.107         True    False
      193         160                 Wilyer Abreu  BOS    ?     3  RF        POSTED      6.59     8.75     10.07 0.152    0.119    34.0     132         3.0          1.00       0.205        False    False
      194         161                 Wilyer Abreu  BOS    ?     3  RF        POSTED      6.59     8.75     10.07 0.152    0.119    34.0     132         3.0          1.00       0.205        False    False
      195         200                 Caleb Durbin  BOS    ?     5  3B        POSTED      6.05     7.87      7.67 0.066    0.052    35.0     122         6.0          0.93       0.213        False    False
      196         201                 Caleb Durbin  BOS    ?     5  3B        POSTED      6.05     7.87      7.67 0.066    0.052    35.0     122         6.0          0.93       0.213        False    False
      197         203              Adley Rutschman  BOS    ?     6   C        POSTED      6.02     7.88      5.53 0.117    0.091    46.0      77         5.0          0.73       0.208        False    False
      198         208            Andruw Monasterio  BOS    ?     6  SS        POSTED      5.93     7.71      5.60 0.059    0.046    36.0      68         8.0          0.87       0.176        False    False
      199         164             Ceddanne Rafaela  BOS    ?     2  CF        POSTED      6.58     8.74      8.07 0.072    0.056    38.0     125         2.0          0.93       0.136        False    False
      200         165             Ceddanne Rafaela  BOS    ?     2  CF        POSTED      6.58     8.74      8.07 0.072    0.056    38.0     125         2.0          0.93       0.136        False    False
      201         257                 Jahmai Jones  BOS    ?     1  DH        POSTED      4.99     5.07      5.80 0.033    0.026    27.0      30         1.0          0.07       0.467        False    False
      202         258                 Jahmai Jones  BOS    ?     1  DH        POSTED      4.99     5.07      5.80 0.033    0.026    27.0      30         1.0          0.07       0.467        False    False
      203         206            Andruw Monasterio  BOS    ?     7  SS        POSTED      5.93     7.71      5.60 0.059    0.046    36.0      68         8.0          0.87       0.176        False    False
      204         207                  Nick Sogard  BOS    ?     8  2B        POSTED      5.93     7.81      9.27 0.054    0.042    25.0      37         1.0          1.00       0.135        False    False
      205         209                  Nick Sogard  BOS    ?     7  2B        POSTED      5.93     7.81      9.27 0.054    0.042    25.0      37         1.0          1.00       0.135        False    False
      206         249                    Eli White  BOS    ?     9  LF        POSTED      5.08     5.62      5.47 0.025    0.020    28.0      40         9.0          0.20       0.300        False    False
      207         250                    Eli White  BOS    ?     9  LF        POSTED      5.08     5.62      5.47 0.025    0.020    28.0      40         9.0          0.20       0.300        False    False
      208         253                  Connor Wong  BOS    ?     8   C        POSTED      5.06     5.84      5.20 0.070    0.055    25.0      57         9.0          0.33       0.281        False    False
      209         155               Bryce Eldridge   SF    ?     4  DH MODAL(last10)      6.64     7.98      9.33 0.092    0.078    35.0      87         4.0          0.80       0.126        False    False
      210         168                 Jung Hoo Lee   SF    ?     6  RF MODAL(last10)      6.50     7.71      5.47 0.076    0.065    37.0     119         6.0          0.80       0.277        False    False
      211         175                 Willy Adames   SF    ?     3  SS MODAL(last10)      6.40     7.54      7.40 0.073    0.062    42.0     123         3.0          0.40       0.252        False    False
      212         214              Osleivis Basabe   SF    ?     6  SS MODAL(last10)      5.77     5.68      3.33 0.045    0.038    26.0      22         5.0          0.80       0.273        False    False
      213         130                Rafael Devers   SF    ?     2  1B MODAL(last10)      7.14     8.67     11.20 0.102    0.087    34.0     137         2.0          1.00       0.190        False    False
      214         204                    Jonah Cox   SF    ?     1  CF MODAL(last10)      5.98     6.07      6.07 0.067    0.057    21.0      15         1.0          0.47       0.400        False    False
      215         212                 Drew Gilbert   SF    ?     1  RF MODAL(last10)      5.82     6.56      9.47 0.037    0.032    30.0      82         1.0          0.67       0.220        False    False
      216         189                Shay Whitcomb   SF    ?     7  3B MODAL(last10)      6.26     7.25      7.25 0.125    0.107    24.0       8         7.0          0.33       0.500         True    False
      217         202                  Turner Hill   SF    ?     7  LF MODAL(last10)      6.05     5.89      5.89 0.000    0.000    15.0       9         7.0          0.60       0.222        False    False
      218         244               Drew Cavanaugh   SF    ?     8   C MODAL(last10)      5.19     4.40      4.27 0.000    0.000    16.0      30         8.0          0.60       0.433        False    False
      219         248               Christian Koss   SF    ?     9  SS MODAL(last10)      5.11     4.28      6.07 0.000    0.000    16.0      32         9.0          1.00       0.312        False    False
      220         211                Isaac Paredes  HOU    ?     3  3B        POSTED      5.86     8.28     10.07 0.088    0.064    31.0     125         3.0          1.00       0.136        False    False
      221         219             Christian Walker  HOU    ?     6  1B        POSTED      5.71     8.02      5.67 0.094    0.068    36.0     127         6.0          0.87       0.220        False    False
      222         236                  Jose Altuve  HOU    ?     4  2B        POSTED      5.38     7.41      6.60 0.065    0.047    41.0     107         4.0          0.93       0.252        False    False
      223         264               Daulton Varsho  HOU    ?     5  CF        POSTED      4.89     6.50      6.07 0.036    0.026    30.0     111         5.0          0.93       0.243        False    False
      224         108               Yordan Alvarez  HOU    ?     2  LF        POSTED      7.50    11.21      9.20 0.195    0.142    39.0     133         2.0          1.00       0.128         True    False
      225         172                  Jeremy Peña  HOU    ?     1  DH        POSTED      6.48     9.69      7.47 0.123    0.089    33.0      81         1.0          0.87       0.136         True    False
      226         259              Taylor Trammell  HOU    ?     7  RF        POSTED      4.96     6.44      4.47 0.055    0.040    25.0      55         7.0          0.67       0.291        False    False
      227         269                   Nick Allen  HOU    ?     8  SS        POSTED      4.77     5.56      5.40 0.031    0.023    31.0      32         8.0          0.27       0.312        False    False
      228         284            Christian Vázquez  HOU    ?     9   C        POSTED      4.43     5.33      4.33 0.015    0.011    20.0      66         9.0          0.47       0.394        False    False
      229         182               Cody Bellinger  NYY    ?     5  LF        POSTED      6.32     8.35      7.33 0.065    0.051    47.0     107         4.0          0.27       0.196        False    False
      230         225           George Lombard Jr.  NYY    ?     6  SS        POSTED      5.64     6.90      5.87 0.050    0.039    22.0      20         6.0          1.00       0.200        False    False
      231         230                 Heliot Ramos  NYY    ?     4  RF        POSTED      5.50     6.89      4.53 0.067    0.052    44.0      89         3.0          0.73       0.247        False    False
      232         239                 Amed Rosario  NYY    ?     3  2B        POSTED      5.30     6.32      3.73 0.080    0.063    40.0      50         3.0          0.07       0.260        False    False
      233         126                     Ben Rice  NYY    ?     2  DH        POSTED      7.19     9.77      8.33 0.185    0.145    39.0     124         2.0          1.00       0.226         True    False
      234         195             Paul Goldschmidt  NYY    ?     1  1B        POSTED      6.15     8.14      5.20 0.081    0.063    29.0      74         1.0          0.13       0.257        False    False
      235         217               José Caballero  NYY    ?     7  3B        POSTED      5.72     7.30      7.27 0.040    0.031    32.0     100         9.0          0.60       0.220        False    False
      236         218                Spencer Jones  NYY    ?     8  CF        POSTED      5.72     7.28      8.87 0.100    0.078    26.0      50         5.0          0.93       0.300        False    False
      237         265                  Ali Sánchez  NYY    ?     9   C        POSTED      4.89     4.23      3.67 0.000    0.000    18.0      22         9.0          0.13       0.409        False    False
      238         242                    Max Muncy  LAD    ?     4  3B        POSTED      5.26     8.88      9.00 0.089    0.055    49.0     112         4.0          0.80       0.196         True    False
      239         268                  Tommy Edman  LAD    ?     5  2B        POSTED      4.80     8.04      6.73 0.078    0.048    31.0      51         5.0          0.87       0.176        False    False
      240         271                  Kyle Tucker  LAD    ?     6  RF        POSTED      4.73     7.71      6.27 0.082    0.051    26.0     122         6.0          0.87       0.197        False    False
      241         276                 Mookie Betts  LAD    ?     3  SS        POSTED      4.63     7.52      8.93 0.104    0.064    38.0      96         5.0          0.93       0.219        False    False
      242         194                Shohei Ohtani  LAD    ?     1  DH        POSTED      6.16    10.76      9.67 0.153    0.095    40.0     124         1.0          1.00       0.121         True    False
      243         252              Freddie Freeman  LAD    ?     2  1B        POSTED      5.07     8.44      6.87 0.099    0.061    30.0     131         2.0          0.93       0.137        False    False
      244         286            Teoscar Hernández  LAD    ?     7  LF        POSTED      4.39     6.97      3.93 0.094    0.058    35.0      96         8.0          0.87       0.312        False    False
      245         298                  Alek Thomas  LAD    ?     9  CF        POSTED      4.13     5.78      5.80 0.031    0.019    25.0      32         8.0          0.27       0.406        False    False
      246         309              Hunter Feduccia  LAD    ?     8   C        POSTED      3.53     4.66      5.47 0.000    0.000    19.0      64         9.0          0.60       0.266        False    False
      247         196               Hunter Goodman  COL    ?     3   C        POSTED      6.10     9.83      7.87 0.157    0.105    46.0     108         4.0          0.27       0.231         True    False
      248         233                 Willi Castro  COL    ?     6  3B        POSTED      5.47     8.52      8.93 0.056    0.037    49.0     107         3.0          0.93       0.150        False    False
      249         243                  TJ Rumfield  COL    ?     4  1B        POSTED      5.22     8.00      6.93 0.057    0.038    29.0     122         4.0          0.80       0.172        False    False
      250         285                 Connor Norby  COL    ?     5  2B        POSTED      4.42     6.22      5.80 0.014    0.009    21.0      72         6.0          0.80       0.181        False    False
      251         213                Jake McCarthy  COL    ?     1  DH        POSTED      5.81     9.22      5.87 0.098    0.065    48.0     112         1.0          1.00       0.161        False    False
      252         226                 Cole Carrigg  COL    ?     2  CF        POSTED      5.61     9.17      5.40 0.121    0.081    29.0      58         2.0          0.87       0.155        False    False
      253         227                Mickey Moniak  COL    ?     7  RF        POSTED      5.56     8.82      5.73 0.143    0.095    36.0      84         2.0          0.87       0.155         True    False
      254         293                  Jordan Beck  COL    ?     8  LF        POSTED      4.28     5.25      5.87 0.000    0.000    19.0      32         7.0          0.47       0.281        False    False
      255         302               Ezequiel Tovar  COL    ?     9  SS        POSTED      4.01     5.54      4.40 0.053    0.035    41.0     114         9.0          0.73       0.316        False    False
      256         223               Wyatt Langford  TEX    ?     3  LF        POSTED      5.67     8.78      8.40 0.111    0.076    27.0      81         3.0          0.93       0.160         True    False
      257         240               Ezequiel Duran  TEX    ?     5  CF        POSTED      5.30     7.91      6.93 0.085    0.058    30.0     118         5.0          1.00       0.271        False    False
      258         251                Brandon Nimmo  TEX    ?     4  RF        POSTED      5.08     7.47      3.27 0.079    0.054    36.0     127         4.0          1.00       0.197        False    False
      259         255                  Jake Burger  TEX    ?     6  1B        POSTED      5.02     7.36      8.53 0.074    0.050    35.0     122         7.0          0.87       0.279        False    False
      260         241                 Corey Seager  TEX    ?     2  SS        POSTED      5.27     7.93      8.80 0.096    0.065    26.0      73         2.0          0.93       0.205         True    False
      261         256                Justin Foscue  TEX    ?     1  2B        POSTED      5.01     7.35      5.80 0.125    0.085    33.0      40         6.0          0.53       0.325        False    False
      262         274                 Cody Freeman  TEX    ?     9  3B        POSTED      4.66     5.23      5.23 0.000    0.000    12.0      13         8.0          0.67       0.077        False    False
      263         278                 Danny Jansen  TEX    ?     7   C        POSTED      4.59     6.12      7.07 0.049    0.033    27.0      41         8.0          0.33       0.293        False    False
      264         303                Logan O'Hoppe  TEX    ?     8  DH        POSTED      3.98     4.96      2.13 0.029    0.020    29.0      69         9.0          0.13       0.362        False    False
      265         192                   Oneil Cruz  PIT    ?     5  CF        POSTED      6.24    11.26     13.13 0.188    0.119    35.0      69         5.0          0.53       0.145         True    False
      266         232               Bryan Reynolds  PIT    ?     3  LF        POSTED      5.49     9.01      6.60 0.111    0.070    38.0     135         3.0          1.00       0.126        False    False
      267         260                Nick Gonzales  PIT    ?     4  DH        POSTED      4.95     7.94      7.27 0.040    0.025    24.0     124         1.0          0.80       0.153        False    False
      268         263                  Jake Mangum  PIT    ?     6  RF        POSTED      4.91     7.89      7.20 0.067    0.043    34.0      90         7.0          0.80       0.189        False    False
      269         234                 Brandon Lowe  PIT    ?     2  2B        POSTED      5.47     9.02      6.33 0.112    0.071    37.0     125         2.0          0.87       0.152         True    False
      270         270              Spencer Horwitz  PIT    ?     1  1B        POSTED      4.76     7.56      3.80 0.048    0.030    26.0      84         1.0          0.67       0.143        False    False
      271         281            Rafael Flores Jr.  PIT    ?     7   C        POSTED      4.49     6.55      7.13 0.136    0.086    36.0      22         5.0          0.80       0.364        False    False
      272         292               Jacob Gonzalez  PIT    ?     8  SS        POSTED      4.29     6.25      3.80 0.062    0.039    38.0      48         8.0          0.53       0.354        False    False
      273         305                 Jared Triolo  PIT    ?     9  3B        POSTED      3.90     5.54      5.60 0.012    0.008    31.0      81         8.0          0.87       0.272        False    False
      274         235              Kevin McGonigle  DET    ?     3  SS        POSTED      5.40     9.12      7.20 0.100    0.062    27.0     130         3.0          1.00       0.115        False    False
      275         238               Dillon Dingler  DET    ?     4  DH        POSTED      5.33     9.02      2.60 0.119    0.074    45.0     118         4.0          0.87       0.195         True    False
      276         254             Eduardo Valencia  DET    ?     5   C        POSTED      5.03    10.00     10.00 0.125    0.078    40.0      16         4.0          0.53       0.250         True    False
      277         282            Spencer Torkelson  DET    ?     6  1B        POSTED      4.47     7.17      4.80 0.063    0.039    32.0     127         7.0          0.93       0.252        False    False
      278         262               Gleyber Torres  DET    ?     1  2B        POSTED      4.92     8.24      7.07 0.067    0.042    28.0      75         1.0          0.93       0.173        False    False
      279         301                   Hao-Yu Lee  DET    ?     2  3B        POSTED      4.02     5.94      6.27 0.031    0.019    22.0      64         2.0          0.80       0.281        False    False
      280         279                    Max Clark  DET    ?     9  CF        POSTED      4.59     7.50      6.00 0.042    0.026    24.0      24         8.0          0.93       0.208        False    False
      281         296                  Ben Malgeri  DET    ?     7  RF        POSTED      4.26     5.78      6.27 0.111    0.069    30.0      18         9.0          0.47       0.278        False    False
      282         299                  Javier Báez  DET    ?     8  LF        POSTED      4.12     5.98      4.73 0.000    0.000    19.0      43         9.0          0.73       0.279        False    False
      283         220                 José Ramírez  CLE    ?     3  3B        POSTED      5.69     9.10      8.13 0.109    0.072    32.0     101         3.0          0.87       0.178        False    False
      284         247               Angel Martínez  CLE    ?     5  LF        POSTED      5.12     7.95      9.73 0.077    0.051    36.0      78         6.0          0.60       0.282         True    False
      285         261                     Jo Adell  CLE    ?     4  RF        POSTED      4.95     7.53     10.20 0.094    0.062    39.0     127         4.0          0.80       0.283         True    False
      286         297                    David Fry  CLE    ?     6  1B        POSTED      4.17     5.31      3.53 0.000    0.000    19.0      42         6.0          0.00       0.286        False    False
      287         231               Chase DeLauter  CLE    ?     2  DH        POSTED      5.50     8.66      9.33 0.091    0.060    33.0     110         2.0          0.60       0.127        False    False
      288         272                  Steven Kwan  CLE    ?     1  CF        POSTED      4.71     7.05      9.00 0.025    0.017    26.0     122         1.0          1.00       0.205        False    False
      289         273                  Angel Genao  CLE    ?     7  2B        POSTED      4.71     6.59      6.07 0.059    0.039    20.0      17         6.0          0.80       0.176        False    False
      290         280               Brayan Rocchio  CLE    ?     9  SS        POSTED      4.53     6.69      4.87 0.054    0.036    24.0     130         9.0          0.80       0.223        False    False
      291         291                Austin Hedges  CLE    ?     8   C        POSTED      4.31     5.95      5.20 0.051    0.034    30.0      59         8.0          0.47       0.254        False    False
      292         267              Julio Rodríguez  SEA    ?     3  CF        POSTED      4.85     7.97      6.47 0.106    0.066    32.0     123         3.0          1.00       0.154        False    False
      293         275                  Josh Naylor  SEA    ?     4  1B        POSTED      4.64     7.54      6.53 0.064    0.040    38.0     125         5.0          0.93       0.184        False    False
      294         288                   Cole Young  SEA    ?     6  2B        POSTED      4.35     6.92      5.60 0.060    0.037    33.0     133         6.0          0.87       0.203        False    False
      295         290                  Cal Raleigh  SEA    ?     5   C        POSTED      4.32     6.82      9.20 0.051    0.032    47.0      99         7.0          0.93       0.242         True    False
      296         266              Dominic Canzone  SEA    ?     2  RF        POSTED      4.89     8.10      9.13 0.118    0.073    30.0     102         3.0          0.93       0.176         True    False
      297         228              Randy Arozarena  SEA    ?     1  LF        POSTED      5.54     9.43     10.67 0.142    0.088    46.0     127         2.0          1.00       0.173        False    False
      298         277                  Taylor Ward  SEA    ?     7  DH        POSTED      4.63     7.51      4.07 0.031    0.019    27.0     130         1.0          0.60       0.108        False    False
      299         283                J.P. Crawford  SEA    ?     8  SS        POSTED      4.44     7.07      5.27 0.070    0.043    37.0      86         8.0          0.20       0.221        False    False
      300         294                 Brock Rodden  SEA    ?     9  3B        POSTED      4.28     5.27      5.27 0.000    0.000    13.0      11         9.0          0.73       0.273        False    False
      301         287               Vaughn Grissom  LAA    ?     3  1B        POSTED      4.37     7.40      7.33 0.073    0.043    30.0      82         4.0          0.93       0.183        False    False
      302         300                    Jose Siri  LAA    ?     4  LF        POSTED      4.03     6.29      5.13 0.073    0.043    20.0      41         5.0          0.47       0.366        False    False
      303         304              Christian Moore  LAA    ?     5  2B        POSTED      3.98     4.45      4.45 0.000    0.000    17.0      11         6.0          0.40       0.182        False    False
      304         306                Oswald Peraza  LAA    ?     6  DH        POSTED      3.88     6.14      3.40 0.066    0.039    33.0      76         7.0          0.27       0.250        False    False
      305         245                   Mike Trout  LAA    ?     2  CF        POSTED      5.19     9.28      7.60 0.129    0.076    36.0     116         2.0          1.00       0.138         True    False
      306         246                    Zach Neto  LAA    ?     1  SS        POSTED      5.13     9.08     11.60 0.123    0.073    43.0     130         1.0          0.93       0.223         True    False
      307         295                 Wade Meckler  LAA    ?     9  RF        POSTED      4.27     7.12      6.07 0.053    0.031    29.0      57         1.0          0.60       0.211        False    False
      308         307                Denzer Guzman  LAA    ?     7  3B        POSTED      3.88     5.96      4.80 0.019    0.011    26.0      54         8.0          0.87       0.204        False    False
      309         308              Travis d'Arnaud  LAA    ?     8   C        POSTED      3.57     3.52      3.07 0.000    0.000    18.0      21         8.0          0.27       0.476        False    False

## QUEUE (36 deep, Appendix A: A bats in law order -> B bats -> ace -> backup arms -> other tiers; blocked names removed)
        type                          name team slot_or_wp  adj_mean_or_k9   max start_rate15
1        BAT  Christian Encarnacion-Strand  BAL         B4           14.11  29.0         0.87
2        BAT              Gunnar Henderson  BAL         B3           13.76  32.0         0.93
3        BAT                Samuel Basallo  BAL         B5           12.57  32.0          0.4
4        BAT                 Dylan Beavers  BAL         B6           12.05  24.0          0.6
5        BAT                   Pete Alonso  BAL         B2           15.79  43.0          1.0
6        BAT              Jackson Holliday  BAL         B1           11.98  24.0          1.0
7        BAT                 Miguel Vargas  CWS         B3           11.83  41.0         0.93
8        BAT             Colson Montgomery  CWS         B6            9.83  32.0         0.93
9        BAT             Braden Montgomery  CWS         B5            9.31  24.0         0.93
10       BAT             Andrew Benintendi  CWS         B4            9.07  30.0         0.73
11         P            Cristopher Sánchez  PHI    wp0.665           10.37  27.0             
12  P-backup                  Cade Cavalli  WSH    wp0.518           10.23  25.0             
13  P-backup                  Nolan McLean  NYM    wp0.537           10.17  21.0             
14       BAT                  Alex Bregman  CHC         B3            9.42  56.0          1.0
15       BAT                 Michael Busch  CHC         B4            9.13  27.0         0.93
16       BAT                  Nico Hoerner  CHC         B5            8.63  34.0         0.93
17       BAT                     Matt Shaw  CHC         B6            8.63  28.0          0.0
18       BAT           Pete Crow-Armstrong  CHC         B1           11.63  46.0          1.0
19       BAT                  Seiya Suzuki  CHC         B2           10.33  34.0          1.0
20       BAT                 Pedro Ramírez  CHC         B8            8.97  32.0         0.93
21       BAT                  Carson Kelly  CHC         B9            8.20  37.0          0.6
22       BAT                 Tyrone Taylor  CHC         B7            7.75  28.0         0.33
23       BAT                  Kody Clemens  MIN         B3           10.23  29.0         0.87
24       BAT                     Josh Bell  MIN         B4            9.90  36.0         0.93
25       BAT                Trevor Larnach  MIN         B6            9.46  26.0          0.6
26       BAT                   Royce Lewis  MIN         B5            9.43  25.0          1.0
27       BAT                    Brooks Lee  MIN         B2            9.61  30.0          1.0
28       BAT                Luke Keaschall  MIN         B1            9.57  24.0          1.0
29       BAT              Kaelen Culpepper  MIN         B7            9.17  16.0         0.93
30       BAT                Walker Jenkins  MIN         B9            9.17   6.0         0.07
31       BAT               Victor Caratini  MIN         B8            8.31  27.0          0.4
32       BAT                    Otto Lopez  MIA         B5           10.65  32.0          1.0
33       BAT                Xavier Edwards  MIA         B3            9.73  25.0          1.0
34       BAT                Griffin Conine  MIA         B4            9.32  33.0          0.8
35       BAT                  Jakob Marsee  MIA         B6            9.26  29.0         0.73
36       BAT           Heriberto Hernández  MIA         B2            9.81  40.0         0.93

## CHECKS: A+B top-10 position mix: {'IF': 6, 'OF': 3, 'DH?': 1} (roster needs 2 IF + 2 OF + flex; DH? = check UD eligibility)
   thin-sample A/B bats: ['Christian Encarnacion-Strand']
   sit-risk A/B bats (start_rate15<0.8): ['Samuel Basallo', 'Dylan Beavers', 'Colton Cowser', 'Andrew Benintendi', 'Jake Rogers']
   Not on this sheet: Underdog tags (green check / B# / Q / O / no-ADP). Tags come from the user's screenshot and override everything here (Rule 12).