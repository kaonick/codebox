from codebox.core.localbox import LocalBox


# regex msg that match No module named 'yfinance'
# if match, return 'yfinance'
def get_uninstall_package(msg:str):
    if "No module named 'yfinance'" in msg:
        return 'yfinance'
    return 'yfinance'


if __name__ == '__main__':
    cbox=LocalBox()
    status=cbox.start()
    print(f"status={status}")

    code="""import yfinance as yf
import matplotlib.pyplot as plt
# Download historical data for desired stocks
tickers = ["AAPL", "META"]
data = yf.download(tickers, start="2020-01-01", end="2022-12-31")
# Normalize the data
data_norm = data['Adj Close'] / data['Adj Close'].iloc[0]
# Plot the data
plt.figure(figsize=(14,7))
for i in range(data_norm.shape[1]):
    plt.plot(data_norm.iloc[:,i], label=tickers[i])
plt.legend(loc='best')
plt.xlabel('Date')
plt.ylabel('Normalized Adj Close Price')
plt.title('Normalized stock prices of AAPL and META')
plt.show()
"""


    ouput=cbox.run("print('hello world')")
    ouput=cbox.run(code)
    print(f"ouput={ouput}")

    package_name=get_uninstall_package(ouput)
    out=cbox.install(package_name=package_name)
    print(f"install out={out}")
    ouput=cbox.run(code)
    print(f"ouput={ouput}")

    # after_install=cbox.install("pip install jupyter_client")
    # print(f"after_install={after_install}")

    restart=cbox.restart()
    print(f"restart={restart}")

    final=cbox.stop()
    print(f"final={final}")
