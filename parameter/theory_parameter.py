import streamlit as st


def content1():
    st.write("")

    st.markdown('<div class="my-custom-text">Generation of Standard Signals and their Statistical Analysis</div>',unsafe_allow_html=True)
    st.divider()
    
    st.markdown('<p class="my-custom-sub-text" >Signal generation is a fundamental concept in Digital Signal Processing (DSP). \
                It involves creating signals with specific characteristics for various applications, such as communication systems, \
                control systems, radar, and biomedical engineering. <br>\
                A signal is a function that conveys information about a physical phenomenon. \
                In DSP, signals are typically represented as discrete-time sequences (sampled data). \
                The ability to generate and manipulate signals digitally allows for advanced signal analysis, filtering, and transformation.</p>',unsafe_allow_html=True)
    
    st.write("")

    st.markdown('<p class="my-custom-sub-text" >This function calculates the following parameters:</p>',unsafe_allow_html=True)
    

    #-------------------1. Mean-----------------------------
    st.markdown('<div class="my-custom-h5-text">1. Mean</div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text" >The mean of a signal is a fundamental statistical measure that represents the average value of the signal over a given time period. \
                It provides insight into the central tendency or the "DC component" of the signal. </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text">If x(t) is a continuous-time signal defined over the interval [0, T], the mean μ is calculated as: </p>',unsafe_allow_html=True)
    
    st.latex(r'''
        μ = \frac{1}{T} \int_{0}^T x(t) dt
             
        ''')
    
    st.markdown('<p class="my-custom-sub-text" >This formula gives the average signal level over time T. </p>',unsafe_allow_html=True)

    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li><b>If μ>0: </b>Signal has a positive bias. </li>\
                <li><b>If μ=0: </b>Signal is centered around zero (zero-mean). </li>\
                <li><b>If μ<0: </b>Signal has a negative bias. </li>\
                </ul>', unsafe_allow_html=True)
    
    
    #-----------------------2. RMS-------------------------

    st.markdown('<div class="my-custom-h5-text">2. RMS</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text">The Root Mean Square (RMS) value of a continuous signal is a fundamental statistical and energy-based measure in signal processing. \
                It provides a measure of the effective magnitude of a varying signal, often used in applications involving power, voltage, current, vibration, and acoustic signals. </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text" >The RMS value of the signal is the normalised second \
                statistical moment of the signal (standard deviation): <br></p>',unsafe_allow_html=True)
    
    st.latex(r'''
        RMS = \sqrt{\frac{1}{T}\int_{0}^T(x(t)-\bar{x})^2 dt}
             
        ''')
    
    

    st.markdown('<p class="my-custom-sub-text" ><br>Where, T is the length of the time record used for the RMS calculation \
                and x&#772; is the mean value of the signal:</p>',unsafe_allow_html=True)
    

    st.latex(r'''
        \bar{x} = \frac{1}{T}\int_{0}^T x(t) dt
             
        ''')
    
    
    
    st.markdown('<p class="my-custom-sub-text" ><br>For discrete (sampled) signals, the RMS of the signal is defined as:</p>',unsafe_allow_html=True)
    
    st.latex(r'''
        RMS = \sqrt{\frac{1}{N}\sum_{n=0}^{N-1}(x(n)-\bar{x})^2}
             
        ''')
    
    st.write("")  # Line break
    st.write("")  # Line break
    
    st.latex(r'''
        \bar{x} = \frac{1}{N}\sum_{n=0}^{N-1} x(n) 
             
        ''')
    
    
    st.markdown('<p class="my-custom-sub-text" ><br>The RMS of the signal is commonly used to describe the \'steady-state\' or \'continuous\' amplitude of a time varying signal.</p>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li>RMS gives a single value representing the signal\'s average power over a given period. </li>\
                <li>Unlike the mean, it accounts for both positive and negative values (since they’re squared), making it especially useful for AC signals or oscillatory data. </li>\
                </ul>',
                unsafe_allow_html=True)
    


    #----------------------3. Standard Deviation--------------------------
    st.markdown('<div class="my-custom-h5-text">3. Standard Deviation</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text" >Standard deviation is a statistical metric that quantifies how much a set of values (signal samples) deviate from their mean (average). \
                In the context of signal processing, it helps to analyse signal variability, stability, and noise characteristics. It is denoted by the symbol σ. </p>',unsafe_allow_html=True)
    
    
    st.markdown('<p class="my-custom-sub-text" >If x(t) is a continuous-time signal defined over a finite interval [0, T], and μ is the mean of the signal: </p>',unsafe_allow_html=True)
    
    st.latex(r'''
         μ = \frac{1}{T} \int_{0}^T x(t) dt
             
        ''')
    
    st.markdown('<p class="my-custom-sub-text" >Then, the standard deviation is:</p>',unsafe_allow_html=True)

    st.latex(r'''
        σ= \sqrt{\frac{1}{T}\int_{0}^T(x(t)- μ)^2 dt}
             
        ''')

    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li><b>Low σ:</b> Signal values are tightly clustered around the mean (e.g., low noise, steady signal). </li>\
                <li><b>High σ:</b> Signal values are widely spread from the mean (e.g., fluctuating, noisy, unstable).</li>\
                <li><b>σ=0:</b> All samples are the same — a constant signal. </li>\
                </ul>', unsafe_allow_html=True)
    

    #-------------------4. Variance-----------------------------
    st.markdown('<div class="my-custom-h5-text">4. Variance</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text" >In signal processing, variance is a key statistical parameter used to measure how much a signal varies with respect to its mean value. \
                It helps in understanding the dispersion, spread, or fluctuation of signal amplitude, making it essential for signal characterization and noise analysis. </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text" >Variance quantifies the average of the squared differences between each value of the signal and its mean. \
                It is denoted by σ<sup>2</sup>, and mathematically it is the square of the standard deviation.  </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text" >Let x(t) be a signal defined over interval [0, T], and μ be the mean, Then the variance is: </p>',unsafe_allow_html=True)
    

    st.latex(r'''
        σ^2 = \frac{1}{T} \int_{0}^T (x(t)-μ)^2 dt
             
        ''')
    


    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li>A low variance implies the signal values are close to the mean (stable signal). </li>\
                <li>A high variance indicates more fluctuation, noise, or variability in the signal. </li>\
                </ul>', unsafe_allow_html=True)


    #-------------------5. Kurtosis-----------------------------
    st.markdown('<div class="my-custom-h5-text">5. Kurtosis</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text">Kurtosis is a statistical measure used to describe the "tailedness" or peakedness of a signal’s amplitude distribution. In signal processing, kurtosis provides insight into how much of the signal’s variance is due to extreme deviations (outliers) rather than more frequent, modest deviations. </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text">For continuous time signals this is defined as:</p>',unsafe_allow_html=True)
    
    st.latex(r'''
        Kurtosis = \frac{\frac{1}{T}\int_{0}^T(x(t)-\bar{x})^4 dt}{(RMS)^4} 
     
        ''')
    
    st.markdown('<p class="my-custom-sub-text"><br>For a continuous signal, it helps in identifying sharp spikes or transient events, which are common in fault detection, vibration analysis, and biomedical signal monitoring. </p>',unsafe_allow_html=True)
    

    st.write("")
    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)
   
    st.markdown('<div class="my-custom-sub-text" style="margin-top:20px">Some definitions subtract 3 to compute excess kurtosis, which compares the distribution to a normal distribution (which has kurtosis = 3).</div>',unsafe_allow_html=True)
 
    st.markdown('<ul class="my-custom-sub-sub-text" >\
                <li>When the kurtosis is equal to 3 (or excess kurtosis is 0), the distribution is called mesokurtic, which represents a normal distribution with moderately sized tails.</li>\
                <li>If the kurtosis is greater than 3 (or excess kurtosis is positive), the distribution is termed leptokurtic. This indicates a sharply peaked distribution with heavier tails, suggesting the presence of more extreme outliers. </li>\
                <li>When the kurtosis is less than 3 (or excess kurtosis is negative), the distribution is known as platykurtic, which is characterized by a flatter peak and lighter tails, indicating fewer extreme deviations from the mean. </li>\
                </ul>',
                unsafe_allow_html=True)


    #-------------------------6. Median-----------------------
    st.markdown('<div class="my-custom-h5-text">6. Median</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text" >The median is a statistical measure that represents the middle value of a signal \
                when all its values are arranged in ascending or descending order. \
                It is a measure of central tendency, like the mean, but is less sensitive to outliers or noise, \
                making it very useful in signal processing, especially for filtering and noise reduction. </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text">For a continuous signal x(t), the median is a value mmm such that: </p>',unsafe_allow_html=True)
    
    st.latex(r'''
         P(x(t) \leq m) = 0.5 
     
        ''')
    
    st.markdown('<p class="my-custom-sub-text"><br>This means that half of the signal\'s amplitude values are less than or equal to \'m\', and the other half are greater than or equal to m.</p>',unsafe_allow_html=True)

    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li>Median gives the center of the distribution of the signal amplitudes. </li>\
                <li>It is robust against outliers and skewed distributions. </li>\
                <li>It is commonly used in non-linear filters and baseline estimation for continuous and sampled signals. </li>\
                </ul>', unsafe_allow_html=True)


    #----------------------7. Mode--------------------------
    st.markdown('<div class="my-custom-h5-text">7. Mode</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text" >The value that occurs most frequently in any distribution curve is called its mode.</p>',unsafe_allow_html=True)



    #------------------------8. Skewness------------------------
    st.markdown('<div class="my-custom-h5-text">8. Skewness</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text" >Skewness is a statistical measure that describes the asymmetry of a signal\'s amplitude distribution about its mean. \
                In signal processing, skewness helps understand whether the signal has a tendency to have more positive or negative deviations from the mean. </p>',unsafe_allow_html=True)
    
    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li><b>Positive skew (right-skewed):</b> Tail on the right side is longer; more values are concentrated on the left. </li>\
                <li><b>Negative skew (left-skewed):</b> Tail on the left side is longer; more values are concentrated on the right. </li>\
                <li><b>Zero skew:</b> Symmetrical distribution, like a normal (Gaussian) distribution. </li>\
                </ul><br>', unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Method to Measure Skewness  </div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text" style="margin-top:10px">Skewness can be measured using Karl Pearson’s Coefficient of Skewness. The formula for measuring skewness using Karl Pearson’s Co-efficient is given below:</p>',unsafe_allow_html=True)
    
    st.write("")

    st.markdown('<p class="my-custom-sub-text">Using Mode, </p>',unsafe_allow_html=True)
    
    st.latex(r'''
        sk_1 = \frac{x- Mode}{S} 
             
        ''')
    
    st.markdown('<p class="my-custom-sub-text">Using Median, </p>',unsafe_allow_html=True)
    
    st.latex(r'''
        sk_2 = \frac{3(x- Median)}{S} 
             
        ''')
    
    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Condition </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li>Mean = Mode = Median, then the coefficient of skewness is zero for symmetrical distribution. </li>\
                <li>Mean > Mode, then the coefficient of skewness will be positive. </li>\
                <li>Mean < Mode, then the coefficient of skewness will be negative. </li>\
                </ul>', unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text" >Karl person`s coefficient of skewness has a positive sign for the positively skewed and a negative sign for the negatively skewed.</p>',unsafe_allow_html=True)
    
    st.write("")
    st.markdown('<div class="my-custom-sub-text" style="font-weight:bold">Interpretation </div>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-sub-text">\
                <li>Skewness measures the asymmetry of the signal\'s amplitude distribution.</li>\
                <li>It is helpful in identifying non-Gaussian behavior, noise characteristics, and feature extraction. </li>\
                <li>In real-world signals, skewness can indicate abnormality, bias, or drift in system behavior. </li>\
                </ul>', unsafe_allow_html=True)



    #-------------------------9. Peak-----------------------
    st.markdown('<div class="my-custom-h5-text">9. Peak</div>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text" >The peak of a continuous signal refers to the maximum absolute value that the signal reaches over a specific time interval. \
                It provides a quick way to understand the extreme value or highest amplitude the signal can attain, which is important in many real-world applications. </p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text">The peak level of the signal is defined simply as half the difference between the maximum and minimum vibration levels:</p>',unsafe_allow_html=True)
    st.latex(r'''
         Peak = \frac{1}{2} (\max(x(t)) - \min(x(t))) 
     
        ''')
