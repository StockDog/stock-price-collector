import pymysql.cursors


def get_all_owned_stocks(db_host, db_user, db_pass, db_name):
    """
    Looks at the StockDog database and
    returns a list of tickers the is collectively owned.
    """
    # Connect to the database
    connection = pymysql.connect(host=db_host,
                                 user=db_user,
                                 password=db_pass,
                                 db=db_name,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            active_portfolio_ids = get_active_portfolios(cursor)
            str_portfolio_ids = ", ".join(map(str, active_portfolio_ids))

            sql = ("SELECT `ticker`, `portfolioId` FROM `PortfolioItem`"
                   "WHERE `portfolioId` in (%s)" % str_portfolio_ids)
            cursor.execute(sql)
            result = cursor.fetchall()

            ticker_list = []

            for row in result:
                ticker_list.append(row["ticker"])

            print("Active tickers:")
            print(list(set(ticker_list)))

            # Return unique elements
            return list(set(ticker_list))
    finally:
        connection.close()


def get_active_portfolios(cursor):
    """Retrieves a list of active portfolio ids"""
    # Get active league ids and convert to sql array format
    active_league_ids = get_active_leagues(cursor)
    str_league_ids = ", ".join(map(str, active_league_ids))

    sql = ("SELECT `id` FROM `Portfolio` "
           "WHERE leagueId IN (%s)" % str_league_ids)
    cursor.execute(sql)
    result = cursor.fetchall()

    portfolio_ids = []

    for row in result:
        portfolio_ids.append(row["id"])

    print("Active portfolios:")
    print(portfolio_ids)

    return portfolio_ids


def get_active_leagues(cursor):
    """Retrieves a list of active league ids"""
    sql = "SELECT `id` FROM `League` WHERE CURDATE() <= END"
    cursor.execute(sql)
    result = cursor.fetchall()

    league_ids = []

    for row in result:
        league_ids.append(row["id"])

    print("Active league ids:")
    print(league_ids)

    return league_ids
