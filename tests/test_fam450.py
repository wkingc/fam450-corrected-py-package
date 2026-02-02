from fam450 import fam450ss, fam450lt, fam450gt
import io
import contextlib
import pytest

def test_fam450ss_initialization():
    x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
    assert{'n': x.n, 'trd': x.trd, 'ovr': x.ovr} == {'n': 158, 'trd': 0.05, 'ovr': 0.1}

def test_fam450ss_allowed_deviations():
    x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
    assert x.allowed_deviations(alt = 'less') == 4
    assert x.allowed_deviations(alt = 'greater') == 11

def test_fam450ss_detailed_results():
    x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
    
    x.allowed_deviations(alt = 'less')
    output_buffer = io.StringIO()
    with contextlib.redirect_stdout(output_buffer):
        x.detailed_results()
    detailed_less = output_buffer.getvalue()
    assert detailed_less == "Null Hypothesis: The true tolerable rate of deviation is 5% or more.\nAlternative Hypothesis: The true tolerable rate of deviation is less than 5%.\n\nIf the experimenter observes 4 deviations or less in a sample size of 158 (2.53%), they can reject with 90% confidence the null hypothesis that the true tolerable rate of deviation is 5% or more in favor of the alternative that it's less than 5%.  If the experimenter observes more than 4 deviations, they fail to reject the null hypothesis, but cannot say the true tolerable rate of deviation is 5% or more.\n"

    x.allowed_deviations(alt = 'greater')
    output_buffer = io.StringIO()
    with contextlib.redirect_stdout(output_buffer):
        x.detailed_results()
    detailed_greater = output_buffer.getvalue()
    assert detailed_greater == "Null Hypothesis: The true tolerable rate of deviation is at most 5%.\nAlternative Hypothesis: The true tolerable rate of deviation is greater than 5%.\n\nIf the experimenter observes more than 11 deviations in a sample size of 158 (6.96%), they can reject with 90% confidence the null hypothesis that the true tolerable rate of deviation is at most 5% in favor of the alternative that it's greater than 5%.  If the experimenter observes 11 or fewer deviations, they fail to reject the null hypothesis, but cannot say the true tolerable rate of deviation is at most 5%.\n"

def test_fam450ss_simple_results():
    x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
    
    x.allowed_deviations(alt = 'less')
    output_buffer = io.StringIO()
    with contextlib.redirect_stdout(output_buffer):
        x.simple_results()
    simple_less = output_buffer.getvalue()
    assert simple_less == "4 is the maximum number of allowed deviations that an experimenter has enough evidence to determine the internal controls are effective.\n"
    
    x.allowed_deviations(alt = 'greater')
    output_buffer = io.StringIO()
    with contextlib.redirect_stdout(output_buffer):
        x.simple_results()
    simple_greater = output_buffer.getvalue()
    assert simple_greater == "11 is the minimum number of allowed deviations, after which an experimenter has enough evidence to determine the internal controls are ineffective.\n"

def test_fam450lt():
    res = fam450lt()
    assert list(res.index) == [45, 78, 105, 132, 158]
    assert list(res.columns) == ['Tolerable Deviation Rate of 5%', 'Tolerable Deviation Rate of 10%']
    assert list(res['Tolerable Deviation Rate of 5%']) == [0, 1, 2, 3, 4]
    assert list(res['Tolerable Deviation Rate of 10%']) == [1, 4, 6, 8, 10]

def test_fam450gt():
    res = fam450gt()
    assert list(res.index) == [45, 78, 105, 132, 158]
    assert list(res.columns) == ['Tolerable Deviation Rate of 5%', 'Tolerable Deviation Rate of 10%']
    assert list(res['Tolerable Deviation Rate of 5%']) == [4, 6, 8, 10, 11]
    assert list(res['Tolerable Deviation Rate of 10%']) == [7, 11, 15, 18, 21]