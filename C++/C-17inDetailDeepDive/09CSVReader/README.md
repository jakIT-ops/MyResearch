## Application Requirements

Imagine you’re working with some sales data and one task is to calculate a sum of orders for some products. Your shopping system is elementary, and instead of a database, you have CSV files with the order data. There’s one file per product.


| date | coupon code | price | discount |  quantity  |
| :--- | ----------- | ----- | -------- | ---------: |
| 5-12-2018 |  | 10.0 | 0 | 2 |
| 5-12-2018 |	| 10.0 | 0 | 1 |
| 6-12-2018 | Santa | 10.0 | 0.25 | 1 |
| 7-12-2018 |	| 10.0 | 0 | 1 |

The application should read the data and then calculate the sum, in the above case we have the following code:

```c++
#include <iostream>
using namespace std;

int main() {
  double sum;
  sum = 10*2+10*1+       // 5th Dec
      10*(1-0.25)*1 +  // 6th Dec with 25% coupon
      10*1;            // 7th Dec
  cout << sum;
}
```

## The Core Parts

### The Main

```c++
int main(int argc, const char** argv) {
    if (argc <= 1)
        return 1;

    try {
        const auto paths = CollectPaths(argv[1]);

        if (paths.empty()) {
            std::cout << "No files to process...\n";
            return 0;
        }

        const auto startDate = argc > 2 ? Date(argv[2]) : Date();
        const auto endDate = argc > 3 ? Date(argv[3]) : Date();

        const auto results = CalcResults(paths, startDate, endDate);

        ShowResults(startDate, endDate, results);
    }
    catch (const std::filesystem::filesystem_error& err) {
        std::cerr << "filesystem error! " << err.what() << '\n';
    }
    catch (const std::runtime_error& err) {
        std::cerr << "runtime  error! " << err.what() << '\n';
    }

    return 0;
}
```

### IsCSVFile

```c++
bool IsCSVFile(const fs::path &p)
{
    return fs::is_regular_file(p) && p.extension() == CSV_EXTENSION;
}

[[nodiscard]] std::vector<fs::path> CollectPaths(const fs::path& startPath)
{
    std::vector<fs::path> paths;
    fs::directory_iterator dirpos{ startPath };
    std::copy_if(fs::begin(dirpos), fs::end(dirpos), std::back_inserter(paths), 
                 IsCSVFile);
    return paths;
}
```


### CalcResult

```c++
struct Result
{
    std::string mFilename;
    double mSum{ 0.0 };
};

[[nodiscard]] std::vector<Result>
CalcResults(const std::vector<fs::path>& paths, Date startDate, Date endDate)
{
    std::vector<Result> results;
    for (const auto& p : paths)
    {
        const auto records = LoadRecords(p);

        const auto totalValue = CalcTotalOrder(records, startDate, endDate);
        results.push_back({ p.string(), totalValue });
    }
    return results;
}
```


