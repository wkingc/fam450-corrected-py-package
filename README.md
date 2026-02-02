# fam450

[![](https://github.com/wkingc/fam450-corrected-py-package/actions/workflows/python-package.yml/badge.svg)](https://github.com/wkingc/fam450-corrected-py-package/actions/workflows/python-package.yml)

[![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A Python package to calculate the number of allowed deviations for tests of internal control effectiveness or ineffectiveness following Financial Audit Manual Section 450.

## Installation

```bash
pip install fam450
```

## Quick Start

```python
from fam450 import fam450ss

# Initialize with sample size of 158, tolerable rate of deviation of 5%, 
# and risk of overreliance of 10%
audit_test = fam450ss(n=158, trd=0.05, ovr=0.1)

# Calculate allowed deviations for testing effectiveness (less than alternative)
max_deviations = audit_test.allowed_deviations(alt='less')
print(f"Maximum allowed deviations for effectiveness: {max_deviations}")

# Display detailed results
audit_test.detailed_results()

# Calculate allowed deviations for testing ineffectiveness (greater than alternative)
min_deviations = audit_test.allowed_deviations(alt='greater')
print(f"Minimum deviations to conclude ineffectiveness: {min_deviations}")

# Display simple results
audit_test.simple_results()
```

## API Reference

### `fam450ss(n, trd, ovr)`

Class for Financial Audit Manual Section 450 sample size calculations.

**Parameters:**

- `n` (int): Sample size
- `trd` (float): Tolerable rate of deviation (as decimal, e.g., 0.05 for 5%)
- `ovr` (float): Risk of overreliance (e.g., 0.1 for 10%, which is 1 - confidence level)

**Methods:**

#### `allowed_deviations(alt)`

Calculate the allowed number of deviations for the given alternative hypothesis.

**Parameters:**
- `alt` (str): Alternative hypothesis ('less' for effectiveness testing, 'greater' for ineffectiveness testing)

**Returns:**
- `int`: Number of allowed deviations

#### `detailed_results()`

Print detailed results of the allowed deviations calculation including hypothesis statements and interpretation.

#### `simple_results()`

Print concise results of the allowed deviations calculation.

### Helper Functions

#### `fam450lt()`

Generate table of allowed deviations for the "less than" alternative hypothesis (testing effectiveness).

**Returns:**
- `pandas.DataFrame`: Table with allowed deviations for various sample sizes and tolerable deviation rates

#### `fam450gt()`

Generate table of allowed deviations for the "greater than" alternative hypothesis (testing ineffectiveness).

**Returns:**
- `pandas.DataFrame`: Table with allowed deviations for various sample sizes and tolerable deviation rates

## Example Output

```python
from fam450 import fam450ss, fam450lt, fam450gt

# Testing internal control effectiveness
audit = fam450ss(n=158, trd=0.05, ovr=0.1)
audit.allowed_deviations(alt='less')
# Returns: 4

audit.simple_results()
# Output: 4 is the maximum number of allowed deviations that an experimenter 
# has enough evidence to determine the internal controls are effective.

audit.detailed_results()
# Null Hypothesis: The true tolerable rate of deviation is 5% or more.
# Alternative Hypothesis: The true tolerable rate of deviation is less than 5%.

# If the experimenter observes 4 deviations or less in a sample size of 
# 158 (2.53%), they can reject with 90% confidence the null hypothesis that 
# the true tolerable rate of deviation is 5% or more in favor of the 
# alternative that it's less than 5%.  If the experimenter observes more 
# than 4 deviations, they fail to reject the null hypothesis, but cannot 
# say the true tolerable rate of deviation is 5% or more.

# Generate FAM 450 tables
effectiveness_table = fam450lt()
print(effectiveness_table)

ineffectiveness_table = fam450gt() 
print(ineffectiveness_table)
```

## Requirements

- Python ≥ 3.9
- scipy
- pandas

## Development

```bash
git clone https://github.com/wkingc/fam450-corrected-py-package.git
cd fam450-corrected-py-package
pip install -e ".[dev]"
python -m pytest
```

## License

MIT License. See [LICENSE](LICENSE) for details.

## Documentation

For a complete usage guide, see <https://www.kingcopeland.com/fam450-corrected-py/>.

## Citation

If you use this package in your work, please consider citing it:

```bibtex
@software{copeland2026fam450,
    author = {Wade K. Copeland},
    title = {{fam450: A Python package to calculate the number of allowed deviations for tests of internal control effectiveness or ineffectiveness}},
    url = {https://pypi.org/project/fam450/},
    version = {0.1.0},
    year = {2026}
}
```
