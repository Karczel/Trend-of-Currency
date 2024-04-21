from ui import UI
from data_handling import get_df

if __name__ == "__main__":
    df = get_df()
    main = UI(df)
    main.run()

