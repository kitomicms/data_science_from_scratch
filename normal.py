import math
import random
import matplotlib.pyplot as plt

# pdf = probability density function
# cdf = cumulative distribution function

def normal_pdf(x,mu=0,sigma=1):
    """mu = mean, sigma = SD """
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2/2/sigma** 2)/(sqrt_two_pi * sigma))

def normal_cdf(x,mu=0,sigma=1):
    """cumulative density function"""
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.0001):
    """find approximate inverse using binary search"""
    
    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
            hi_z, hi_p = mid_z, mid_p
        else:
            break
            
    return mu + sigma * mid_z



if __name__ == '__main__':
    xs = [x / 10.0 for x in range(-50,50)]
    
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.show()
    
    xs = [x / 10.0 for x in range(-50,50)]
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
    plt.legend(loc=4)
    plt.title("Various Normal cdfs")
    plt.show()
    
    inverse_normal_cdf(0.25)
    inverse_normal_cdf(0.5)
    inverse_normal_cdf(0.66)
    inverse_normal_cdf(0.9)
    inverse_normal_cdf(0.95)
    inverse_normal_cdf(0.99)
    
    n = 10000
    sum(random.gauss(0,1) <= )
    