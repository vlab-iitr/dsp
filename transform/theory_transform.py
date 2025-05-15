import streamlit as st

def content5():

    st.markdown('<div class="my-custom-text">Spectral Analysis of Signals using Signal Transform Functions</div>',unsafe_allow_html=True)
    st.divider()
    st.write('<p class="my-custom-sub-text">Transforms are fundamental tools in Digital Signal Processing (DSP) that \
             allow signals to be analyzed and processed in different domains. The most commonly used transforms in DSP \
             convert signals from the time domain to the frequency domain, making it easier to analyze frequency components, \
             filter signals, and compress data.<br> A signal in the time domain describes how it changes over time, whereas in the \
             frequency domain, it represents how much of each frequency is present.</p>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">Types of Transforms in DSP</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">There are several important transforms used in signal processing, image processing, and communication systems:</p>',unsafe_allow_html=True)

    #----------------------------------------#
    st.markdown('<div class="my-custom-h5-text">1. Fast Fourier Transform (FFT)</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">An FFT computes the Discrete Fourier Transform (DFT) and produces exactly the same result as evaluating the DFT definition directly;\
              the only difference is that an FFT is much faster. The basic idea is to break up a transform of length\
              into two transforms of length using the identity.</p>',unsafe_allow_html=True)

    st.latex(r'''
        \displaystyle\sum_{n=0}^{N-1} a_ne^{\frac{-2\pi i}{N}k n} = \displaystyle\sum_{n=0}^{\frac{N}{2}-1} a_{2n}e^{\frac{-2\pi i}{N}k 2n} + \displaystyle\sum_{n=0}^{\frac{N}{2}-1} a_{2n+1}e^{\frac{-2\pi i}{N}k (2n+1)}
        
        ''')

    st.latex(r'''
                \space\space  \space\space \space\space \space\space \space\space \space\space \space\space  \space\space \space\space \space\space \space\space= \displaystyle\sum_{n=0}^{\frac{N}{2}-1} a_{n}^{even} e^{\frac{-2\pi i}{\frac{N}{2}}k n} + e^{\frac{-2\pi i}{N}k} \displaystyle\sum_{n=0}^{\frac{N}{2}-1} a_{n}^{odd}e^{\frac{-2\pi i}{\frac{N}{2}}k n}

        ''')

    st.write('<p class="my-custom-sub-text">Since the fourier transform gives the information about the frequency component of any signal, it is \
             used for finding out what are the frequencies present in the signal if the signal is stationary i.e. \
             the frequency component of the signal is not changing with time.</p>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">The inverse fourier transform finds the time-domain representation from the frequency domain.</p>',unsafe_allow_html=True)
    st.write('<p class="my-custom-sub-text">For a function F:</p>',unsafe_allow_html=True)

    st.latex(r'''
                F(s) = S(f) 

        ''')
    st.latex(r'''
             \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space
            \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space
            \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space 
            \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space
            \space\space  \space\space \space\space  \space\space \space\space  \space\space= \int_{-\infty}^\infty s(t)e(-i)2\pi ft dt 
  
        ''')


    st.latex(r'''
                F^{-1}(s) = s(t) 

        ''')

    st.latex(r'''
                 \space\space \space\space  \space\space \space\space  \space\space \space\space
            \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space
            \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space 
            \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space
            \space\space  \space\space \space\space  \space\space \space\space  \space\space \space\space  \space\space 
            = \int_{-\infty}^\infty S(f)e(i)2\pi ft df 
    
        ''')

    st.markdown('<p class="my-custom-sub-text">Equation 1 shows Fourier transform of signal F \
                whereas equation 2 shows the inverse Fourier transform.</p>',unsafe_allow_html=True)


    #----------------------------------------------------------------#
    st.markdown('<div class="my-custom-h5-text">2. Discrete Cosine Transform (DCT)</div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text">A DCT expresses a sequence of finitely many  data points in terms of a sum of cosine functions oscillating at different frequencies. \
                DCTs are important to numerous applications in science and engineering, from  lossy compression of \
                audio and images (where small high-frequency components can be discarded), to  spectral methods for \
                the numerical solution of partial differential equations. The use of cosine rather than  sine functions\
                 is critical in these applications: for compression, it turns out that cosine functions are much more efficient \
                (as explained below, fewer are needed to approximate a typical  signal), whereas for differential equations the cosines express a particular choice of  boundary conditions.</p>' ,unsafe_allow_html=True)
    

    st.markdown('<p class="my-custom-sub-text">The Discrete Cosine Transform (DCT) {X} of a sequence X \
                is defined by the following equations: </p>',unsafe_allow_html=True)

    st.latex(r'''
                y_k = \sqrt{\frac{2}{N}}a_k \displaystyle\sum_{n=0}^{N-1} x_n \frac{\cos(2n+1)k\Pi}{2N}
    
        ''')
    
    st.markdown('<center>and</center>',unsafe_allow_html=True)

    st.latex(r'''
                a_k = \begin{cases}
   \frac{1}{\sqrt2} &\text{for } k = 0 \\
   1 &\text{for } k = 1, 2...n-1
\end{cases}
    
        ''')
    
    st.markdown('<p class="my-custom-sub-text">Where, N is the length of X, x<sub>n</sub> is the n<sup>th</sup> element of X,\
                 y<sub>k</sub> is the k<sup>th</sup> element of DCT {X}</p>',unsafe_allow_html=True)


    #----------------------------------------------------------------#
    st.markdown('<div class="my-custom-h5-text">3. Discrete Sine Transform (DST)</div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text">The DST \
                {X} of a sequence X is defined by the following equations:</p>',unsafe_allow_html=True)

    
    st.latex(r'''
                y_k = \displaystyle\sum_{n=0}^{N-1} x_n \frac{\sin\Pi(n+1)(k+1)}{N+1}  \space \space  , k = 0, 1, 2...n-1
    
        ''')
    
    st.markdown('<p class="my-custom-sub-text">Where N is the length of the input sequence X, x<sub>n</sub> is the n<sup>th</sup>\
                 element of the input sequence X, and y<sub>k</sub> is the k<sup>th</sup> element of the output sequence DST {X}.</p>',unsafe_allow_html=True)
    
    
    #----------------------------------------------------------------#

    st.markdown('<div class="my-custom-h5-text">4. Hilbert Transform</div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text">In mathematics and in signal processing, \
                the Hilbert transform is a linear operator which takes a function, u(t), and produces a function, H(u)(t), with the same domain. \
                The Hilbert transform is named after David Hilbert, who first introduced the operator in \
                order to solve a special case of the Riemann–Hilbert problem for holomorphic functions. \
                It is a basic tool in Fourier analysis, and provides a concrete means for realizing the \
                conjugate of a given function or Fourier series. Furthermore, in harmonic analysis, \
                it is an example of a singular integral operator, and of a Fourier multiplier.</p>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text">The Hilbert transform is also important in the field of signal processing where it is\
                 used to derive the analytic representation of a signal u(t). The Hilbert transform can\
                 be thought of as the convolution of u(t) with the function h(t) = 1/(3.14*t), and is given by:</p>',unsafe_allow_html=True)

    st.latex(r'''
                H(u)(t) = p.v.\int_{-\infty}^\infty u(\tau)h(t-\tau)d\tau = \frac{1}{\pi} p.v. \int_{-\infty}^\infty \frac{u(\tau)}{t-\tau}d\tau
    
        ''')
    
    
    #----------------------------------------------------------------#

    st.markdown('<div class="my-custom-h5-text">5. Wavelet Transform (WT)</div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text">In numerical analysis and functional analysis, a Discrete Wavelet Transform (DWT) is any wavelet transform for which the wavelets are discretely sampled. \
                As with other wavelet transforms, a key advantage it has over Fourier transforms is temporal resolution: \
                it captures both frequency and location information (location in time). \
                The wavelet transform replaces the Fourier transform\'s sinusoidal waves by a family \
                generated by translations and dilations of a window called a wavelet.</p>',unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;">It includes two types of wavelets:</p>',unsafe_allow_html=True)
    
    
    st.markdown('<ul class="my-custom-sub-text">\
                <li>orthogonal (Haar, Daubechies (dbxx), Coiflets (coifx), Symmlets (symx))</li>\
                <li>biorthogonal (Biorthogonal (biorx_x), including FBI (bior4_4 (FBI)))</li>\
                </ul>',unsafe_allow_html=True)
    
    st.markdown('<p class="my-custom-sub-text">where, x indicates the order of the wavelet.</p>',unsafe_allow_html=True)
    st.markdown('<p class="my-custom-sub-text">The higher the order, the smoother the wavelet.</p>',unsafe_allow_html=True)

     
    #----------------------------------------------------------------#

    st.markdown('<div class="my-custom-h5-text">6. Chirp-Z Transform (CZT)</div>',unsafe_allow_html=True)


    st.markdown('<p class="my-custom-sub-text">Bluestein\'s FFT algorithm, commonly called the chirp-z transform algorithm, \
                is a FFT algorithm that computes the DFT \
                of arbitrary sizes (including prime sizes) by re-expressing the DFT as a convolution.</p>',unsafe_allow_html=True)

