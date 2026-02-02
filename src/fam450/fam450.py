from scipy.stats import binomtest
import pandas as pd

class fam450ss:
    """Class object for the Financial Audit Manual Section 450 sample size calculator.
    
    Attributes:
        n (int): Sample size.
        trd (float): Tolerable rate of deviation.
        ovr (float): Risk of overreliance (e.g., 1 - confidence level).
        k (int): Allowed number of deviations.  For the less than 
        alt (str): Alternative hypothesis ('less' or 'greater')
    """
    
    def __init__(self, n, trd, ovr):
        """Initialize the fam450 class object.
        
        Args:
            n (int): Sample size.
            trd (float): Tolerable rate of deviation.
            ovr (float): Risk of overreliance (e.g., 1 - confidence level).
        
        Attributes:
            n (int): Sample size.
            trd (float): Tolerable rate of deviation.
            ovr (float): Risk of overreliance (e.g., 1 - confidence level).
        
        Returns:
            None
        
        Raises:
            None
        
        Example:
            >>> x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
            >>> {'n': x.n, 'trd': x.trd, 'ovr': x.ovr}
            {'n': 158, 'trd': 0.05, 'ovr': 0.1}
        """
        self.n = n
        self.trd = trd
        self.ovr = ovr
    
    def allowed_deviations(self, alt):
        """Calculate the allowed number of deviations for the given alternative hypothesis.
        
        Args:
            alt (str): Alternative hypothesis ('less' or 'greater')
        
        Attributes:
            alt (str): Alternative hypothesis ('less' or 'greater')
            k (int): Allowed number of deviations.
        
        Returns:
            int: Allowed number of deviations.
        
        Raises:
            ValueError: If the alternative hypothesis is not 'less' or 'greater'.
        
        Example:
            >>> x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
            >>> x.allowed_deviations(alt = 'less')
            4
            >>> x.allowed_deviations(alt = 'greater')
            11
        """
        k = 0
        
        if alt == 'less':
            while not (binomtest(k = k, n = self.n, p = self.trd, alternative = alt).pvalue < self.ovr and binomtest(k = k + 1, n = self.n, p = self.trd, alternative = alt).pvalue >= self.ovr):
                k = k + 1
            
            self.alt = alt
            self.k = k
            
            return k
        elif alt == 'greater':
            while not (binomtest(k = k, n = self.n, p = self.trd, alternative = alt).pvalue >= self.ovr and binomtest(k = k + 1, n = self.n, p = self.trd, alternative = alt).pvalue < self.ovr):
                k = k + 1
            
            self.alt = alt
            self.k = k
            
            return k
        else:
            raise ValueError(f"Unsupported alternative: {alt}")
    
    def detailed_results(self):
        """Print detailed results of the allowed deviations calculation.
        
        Args:
            None
        
        Attributes:
            None
            
        Returns:
            None
            
        Raises:
            ValueError: If allowed_deviations() has not been run yet.
        
        Example:
            >>> x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
            >>> x.allowed_deviations(alt = 'less')
            4
            >>> x.detailed_results()
            Null Hypothesis: The true tolerable rate of deviation is 5% or more.
            Alternative Hypothesis: The true tolerable rate of deviation is less than 5%.

            If the experimenter observes 4 deviations or less in a sample size of 158 (2.53%), they can reject with 90% confidence the null hypothesis that the true tolerable rate of deviation is 5% or more in favor of the alternative that it's less than 5%.  If the experimenter observes more than 4 deviations, they fail to reject the null hypothesis, but cannot say the true tolerable rate of deviation is 5% or more.
            >>> x.allowed_deviations(alt = 'greater')
            11
            >>> x.detailed_results()
            Null Hypothesis: The true tolerable rate of deviation is at most 5%.
            Alternative Hypothesis: The true tolerable rate of deviation is greater than 5%.

            If the experimenter observes more than 11 deviations in a sample size of 158 (6.96%), they can reject with 90% confidence the null hypothesis that the true tolerable rate of deviation is at most 5% in favor of the alternative that it's greater than 5%.  If the experimenter observes 11 or fewer deviations, they fail to reject the null hypothesis, but cannot say the true tolerable rate of deviation is at most 5%.
        """
        if not hasattr(self, 'alt') or not hasattr(self, 'k'):
            raise ValueError("You must run allowed_deviations() before detailed_results().")
        
        if self.alt == 'less':
            print(f"Null Hypothesis: The true tolerable rate of deviation is {self.trd:.0%} or more.\nAlternative Hypothesis: The true tolerable rate of deviation is less than {self.trd:.0%}.\n\nIf the experimenter observes {self.k:,} deviations or less in a sample size of {self.n:,} ({self.k/self.n:.2%}), they can reject with {1-self.ovr:.0%} confidence the null hypothesis that the true tolerable rate of deviation is {self.trd:.0%} or more in favor of the alternative that it's less than {self.trd:.0%}.  If the experimenter observes more than {self.k:,} deviations, they fail to reject the null hypothesis, but cannot say the true tolerable rate of deviation is {self.trd:.0%} or more.")
        
        if self.alt == 'greater':
            print(f"Null Hypothesis: The true tolerable rate of deviation is at most {self.trd:.0%}.\nAlternative Hypothesis: The true tolerable rate of deviation is greater than {self.trd:.0%}.\n\nIf the experimenter observes more than {self.k:,} deviations in a sample size of {self.n:,} ({self.k/self.n:.2%}), they can reject with {1-self.ovr:.0%} confidence the null hypothesis that the true tolerable rate of deviation is at most {self.trd:.0%} in favor of the alternative that it's greater than {self.trd:.0%}.  If the experimenter observes {self.k:,} or fewer deviations, they fail to reject the null hypothesis, but cannot say the true tolerable rate of deviation is at most {self.trd:.0%}.")
    
    def simple_results(self):
        """Print simple results of the allowed deviations calculation.
        
        Args:
            None
            
        Attributes:
            None
        
        Returns:
            None
        
        Raises:
            ValueError: If allowed_deviations() has not been run yet.
            
        Example:
            >>> x = fam450(n = 158, trd = 0.05, ovr = 0.1)
            >>> x.allowed_deviations(alt = 'less')
            4
            >>> x.simple_results()
            4 is the maximum number of allowed deviations that an experimenter has enough evidence to determine the internal controls are effective.
            
            >>> x.allowed_deviations(alt = 'greater')
            11
            >>> x.simple_results()
            11 is the minimum number of allowed deviations, after which an experimenter has enough evidence to determine the internal controls are ineffective.
        """
        
        if not hasattr(self, 'alt') or not hasattr(self, 'k'):
            raise ValueError("You must run allowed_deviations() before simple_results().")
        
        if self.alt == 'less':
            print(f"{self.k:,} is the maximum number of allowed deviations that an experimenter has enough evidence to determine the internal controls are effective.")
        
        if self.alt == 'greater':
            print(f"{self.k:,} is the minimum number of allowed deviations, after which an experimenter has enough evidence to determine the internal controls are ineffective.")

def fam450lt():
    """Reproduce tables 1 and 2 from FAM 450 for the less than alternative hypothesis.  The overreliance risk is set to 10%.
    
    Returns:
        pd.DataFrame: DataFrame containing allowed deviations for various sample sizes and tolerable rates of deviations.
    """
    x = fam450ss(n = 45, trd = 0.05, ovr = 0.1)
    r11 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 45, trd = 0.1, ovr = 0.1)
    r12 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 78, trd = 0.05, ovr = 0.1)
    r21 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 78, trd = 0.1, ovr = 0.1)
    r22 = x.allowed_deviations(alt = 'less')
   
    x = fam450ss(n = 105, trd = 0.05, ovr = 0.1)
    r31 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 105, trd = 0.1, ovr = 0.1)
    r32 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 132, trd = 0.05, ovr = 0.1)
    r41 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 132, trd = 0.1, ovr = 0.1)
    r42 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
    r51 = x.allowed_deviations(alt = 'less')
    
    x = fam450ss(n = 158, trd = 0.1, ovr = 0.1)
    r52 = x.allowed_deviations(alt = 'less')
    
    res = {'45': (r11, r12), '78': (r21, r22), '105': (r31, r32), '132': (r41, r42), '158': (r51, r52)}
    res = pd.DataFrame.from_dict(res, orient = 'index', columns = ['Tolerable Deviation Rate of 5%', 'Tolerable Deviation Rate of 10%'])
    res.index.name = 'Sample Size'
    res.index = res.index.astype(int)
    
    return res

def fam450gt():
    """Reproduce tables 1 and 2 from FAM 450 for the greater than alternative hypothesis.
    
    Returns:
        pd.DataFrame: DataFrame containing allowed deviations for various sample sizes and tolerable rates of deviations.
    """
    x = fam450ss(n = 45, trd = 0.05, ovr = 0.1)
    r11 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 45, trd = 0.1, ovr = 0.1)
    r12 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 78, trd = 0.05, ovr = 0.1)
    r21 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 78, trd = 0.1, ovr = 0.1)
    r22 = x.allowed_deviations(alt = 'greater')
   
    x = fam450ss(n = 105, trd = 0.05, ovr = 0.1)
    r31 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 105, trd = 0.1, ovr = 0.1)
    r32 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 132, trd = 0.05, ovr = 0.1)
    r41 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 132, trd = 0.1, ovr = 0.1)
    r42 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 158, trd = 0.05, ovr = 0.1)
    r51 = x.allowed_deviations(alt = 'greater')
    
    x = fam450ss(n = 158, trd = 0.1, ovr = 0.1)
    r52 = x.allowed_deviations(alt = 'greater')
    
    res = {'45': (r11, r12), '78': (r21, r22), '105': (r31, r32), '132': (r41, r42), '158': (r51, r52)}
    res = pd.DataFrame.from_dict(res, orient = 'index', columns = ['Tolerable Deviation Rate of 5%', 'Tolerable Deviation Rate of 10%'])
    res.index.name = 'Sample Size'
    res.index = res.index.astype(int)
    
    return res