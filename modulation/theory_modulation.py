import streamlit as st
from PIL import Image

def content7():
    st.markdown('<div class="my-custom-text">Study and Demonstrate the Amplitude, Frequency and Phase Modulation</div>',unsafe_allow_html=True)
    st.divider()
    
    image_path1 = 'modulation/images/amp.png'  # Replace with your image path
    image = Image.open(image_path1)
    def image_to_base64(image_path):
        import base64
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    st.markdown('<div class="my-custom-h5-text">1. Amplitude Modulation (AM)</div>',unsafe_allow_html=True)

    st.markdown('<p class="my-custom-sub-text">Amplitude modulation, or AM, is a modulation \
             technology mainly used for radio carrier wave-based message transmission. \
             Amplitude modulation modifies the carrier wave\'s amplitude (signal intensity) \
             in accordance with the message signal, such as an audio signal, i.e., a modulating signal. \
             The mechanism of AM can be: </p>\
             <ul class="my-custom-sub-text">\
             <li>A complex interaction between modulating waves and carrier signals is the basis of AM. </li>\
             <li>By means of a rigorous modulation procedure, information is encoded for transmission by the carrier wave\'s amplitude, which experiences minute variations in response to the modulating signal. </li>\
             <li>Demodulation techniques use complex circuitry to accurately detect and amplify the modulating waveform; these techniques are crucial for recovering the original signal from AM transmissions. </li>\
             <li>In simple terms, AM works by altering the height/magnitude of the carrier wave to match the information we want to send, then changing it back at the other end to hear or see the message. </li>\
              </ul>\
             <figure style="text-align: center;">\
               <img src="data:image/png;base64,{}" alt="Centered Image"><br>\
              <figcaption style="font-size:18px;font-weight:bold;font-family: Georgia, serif;">Fig.1 Block Diagram of Amplitude Modulation</figcaption>\
            </figure>\
             '.format(image_to_base64(image_path1)),unsafe_allow_html=True)
    

    image_path2 = 'modulation/images/amp_signal.png'  # Replace with your image path
    image = Image.open(image_path2)
    st.markdown('<div class="my-custom-h5-text">1.1 Terms Related to Amplitude Modulation </div>\
                <p class="my-custom-sub-text">Following terms are related to amplitude modulation:  </p>\
                <ol type="a" class="my-custom-sub-text">\
                <li><b>Carrier Wave</b>\
                <p class="my-custom-sub-text">A carrier wave is a pure wave of constant frequency analogous to a sine wave of electronic signal. \
                It doesn\'t carry much information itself that we can relate to (such as speech or data). </p>\
                </li>\
                <li><b>Modulating Signal</b>\
                <p class="my-custom-sub-text">To include speech information or data information to the carrier wave which can be \
                interpreted, another wave needs to be imposed, called an input signal, on top of the carrier wave. \
                This input signal is known as the modulating signal.</p>\
                </li>\
                <li><b>Modulation</b>\
                <p class="my-custom-sub-text">Modulation is defined as the process of superimposing a low-frequency signal which is coined as the input \
                    signal or modulating signal on a high-frequency carrier signal whose data or speech needs to be interpreted.</p>\
                </li>\
                <li><b>Amplitude Phase</b>\
                <p class="my-custom-sub-text">Amplitude is the maximum distance from the centre line to the peak; phase, on the other hand, tells us where any particle in a periodic waveform is located, \
             and frequency is the number of waves passing through a given point in a second.</p>\
                <ul class="my-custom-sub-text">\
             <li>Amplitude modulation alters the carrier wave\'s magnitude to convey information, which is then restored at the receiver to interpret the message. </li>\
             <li>In contrast, Frequency modulation adjusts the carrier wave\'s frequency, allowing data and speech information to be transmitted via frequency changes. </li>\
             <li>Similarly, phase modulation varies the carrier wave\'s phase to convey data and speech information. Each modulation technique offers unique methods for encoding and transmitting information. </li>\
            </ul>\
            </li>\
            </ol>\
            <figure style="text-align: center;">\
            <img src="data:image/png;base64,{}" alt="Centered Image"><br>\
            <figcaption style="font-size:18px;font-weight:bold;font-family: Georgia, serif;">Fig. 2 Representation of Amplitude Modulation Signal</figcaption>\
            </figure><br>\
             '.format(image_to_base64(image_path2)),unsafe_allow_html=True)

      
    #--------------------------------------#

    st.markdown('<div class="my-custom-h5-text">1.2 Expression for Amplitude Modulated Wave  </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Carrier wave will be generally a high frequency wave and similar to sine or cosine wave and can be represented as:</p>',unsafe_allow_html=True)

    st.latex(r'''
        C(t) = A_csin\omega_ct
        
        ''')
    
    st.write('<p class="my-custom-sub-text">or</p>',unsafe_allow_html=True)


    st.latex(r'''
        C(t) = A_csin(2\pi f_ct)
        
        ''')
    
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li>A<sub>c</sub> is the amplitude of carrier wave,</li>\
                <li>sinω<sub>c</sub>t is the phase of carrier wave,</li>\
                <li>f<sub>c</sub> is the frequency of carrier wave,</li>\
                <li>C(t) is our carrier wave.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.write('<p class="my-custom-sub-text">Modulating signal is also analogous to a sine or cosine wave and represented as: </p>',unsafe_allow_html=True)

    st.latex(r'''
        m(t) = A_msin\omega_mt
        
        ''')
    
    st.write('<p class="my-custom-sub-text">or</p>',unsafe_allow_html=True)


    st.latex(r'''
        m(t) = A_msin(2\Pi f_mt)
       
        ''')
    
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li>A<sub>m</sub> is the amplitude of modulating wave,</li>\
                <li>sinω<sub>m</sub>t is the phase of modulating wave, </li>\
                <li>f<sub>m</sub> is the frequency of modulating signal,</li>\
                <li>m(t) is our modulating or input signal.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.write('<p class="my-custom-sub-text">We are now superimposing modulating signal into a carrier wave to interpret the data \
             and speech information and thus also varying the amplitude of the carrier wave in accordance with the amplitude of the modulating signal, and hence the amplitude-modulated wave Cm(t) will be: </p>',unsafe_allow_html=True)

    st.latex(r'''
        C_m(t) = (A_c + A_m sin\omega_mt) sin \omega_ct
        
        ''')
    
    st.write('<p class="my-custom-sub-text">This is the general form of an amplitude-modulated wave.</p>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">The degree of modulation is given by index of modulation. Taking A<sub>c</sub> common in (3), we get </p>',unsafe_allow_html=True)

    st.latex(r'''
        C_m(t) = A_c\left(1 + \left( \frac{A_m}{A_c}\right) sin(\omega_mt)\right)sin(\omega_ct)
        
        ''')
    
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li><b>A<sub>m</sub>/A<sub>c</sub> = μ</b> which is known as modulation index also known as modulation factor, modulation coefficient or degree of modulation.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.write('<p class="my-custom-sub-text">Thus, modulation index is defined as the ratio of the amplitude of the modulating signal to the amplitude of the carrier wave.</p>',unsafe_allow_html=True)

    st.markdown('<div class="my-custom-h5-text">1.3 Types Of Amplitude Modulation   </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Amplitude Modulation can be categorized into three main domains: </p>',unsafe_allow_html=True)

    st.markdown('<ol class="my-custom-sub-text">\
                <li><b>Double sideband-suppressed carrier modulation (DSB-SC):</b> In this, the frequency spectrum of the modulating signal is symmetrically below and above that of the carrier signal. Sidebands are represented by the incoming information signal\'s lower and upper frequencies. Higher frequency components are found in upper sidebands compared to lower sidebands and lower frequency components in carrier frequencies. </li>\
                <li><b>Modulation of a single sideband (SSB):</b> Amplification of single sideband refers to the transmission of only one sideband through an antenna. It has a sideband on either the top or lower half. </li>\
                <li><b>Modulation of the Vestigial Sideband (VSB):</b> It is a solution to the problem of distracting noises created because of bandpass filter not having the capacity to block off frequencies outside of the cut off zone. In this instance, one of the sidebands (upper or lower) is transmitted but a part of the other is not. </li>\
                </ol>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">1.4 Advantages and Disadvantages of AM</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Different amplitude modulation techniques have their own advantages and disadvantages as mentioned below:</p>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text">\
                <li><b>DSB-SC:</b> It has lower power consumption, and it is simple technique of modulation. But it is complex in detection at AM receiver. It is used in analog TV transmission systems to transmit color information.</li>\
                <li><b>SSB-SC:</b> It is used for efficient management of spectrum. But generation of SSB modulation is difficult and it is complex in detection at receiver. It is used for 2-way radio FDM. </li>\
                <li><b>VSB-SC:</b> It is compromise between DSB and SSB types. But demodulation system is complex. Bandwidth of VSB-SC is 25% higher than SSB-SC. It is used for analog TV broadcast systems. </li>\
                </ul>',unsafe_allow_html=True)
    


    #---------------------Frequency Modulation--------------------------#
    st.markdown('<div class="my-custom-h5-text">2. Frequency Modulation (FM)</div>',unsafe_allow_html=True)

    image_path3 = 'modulation/images/frq.png'  # Replace with your image path
    image = Image.open(image_path3)
    image_path4 = 'modulation/images/fre_phase.png'  # Replace with your image path
    image = Image.open(image_path4)
    st.write('<p class="my-custom-sub-text">Frequency Modulation is a process of encoding information on one carrier wave by changing its frequency. \
             The frequency of the carrier wave is changed according to the frequency of the modulating signal.\
             Frequency modulation is used for broadcasting and radio communication. Modulation is the process of converting the carrier signal into an electrical signal. \
             Amplitude and phase remain the same in FM.</p>'\
            '<p class="my-custom-sub-text">Frequency Modulation is used in FM radio broadcasting, magnetic \
            tape-recording systems, monitoring newborns for seizures via EEG, radar, seismic prospecting, sound synthesis, \
            telemetry, two-way radio systems, and video-transmission systems. </p>\
            <figure style="text-align: center;">\
                <img src="data:image/png;base64,{}" alt="Centered Image"><br>\
                <figcaption style="font-size:18px;font-weight:bold;font-family: Georgia, serif;">Fig. 3 Block Diagram of Frequency Modulation</figcaption>\
            </figure><br>\
             '.format(image_to_base64(image_path3)),unsafe_allow_html=True)
    
    st.write('<figure style="text-align: center;">\
                <img src="data:image/png;base64,{}" alt="Centered Image"><br>\
                <figcaption style="font-size:18px;font-weight:bold;font-family: Georgia, serif;">Fig. 4 Representation of Frequency Modulation Signal</figcaption>\
            </figure><br>\
             '.format(image_to_base64(image_path4)),unsafe_allow_html=True)

    st.markdown('<div class="my-custom-h5-text">2.1 Expression for Frequency Modulated Wave </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">The expression for a frequency modulated wave can be derived from the basic equation for frequency modulation. The general form of an FM wave can be written as </p>',unsafe_allow_html=True)

    st.latex(r'''
        s(t) = A_ccos \left(2\pi f_ct + 2\pi k_f \int_{0}^t m(\tau)d\tau \right )
        
        ''')
    
   
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li>A<sub>c</sub> is the Amplitude of the Carrier Signal,</li>\
                <li>f<sub>c</sub> is the Frequency of the Carrier Signal,</li>\
                <li>k<sub>f</sub> is the Frequency Deviation Sensitivity,</li>\
                <li>m(t) is the Modulating Signal.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">2.2 Modulation Index</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Modulation index is denoted by μ. It is the ratio of the amplitude of modulating signal to that of the carrier signal. </p>',unsafe_allow_html=True)

    st.latex(r'''
        \mu = \frac{A_m}{A_c}

        ''')
    
    st.markdown('<div class="my-custom-h5-text">2.3 Expression For Frequency Modulation</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">We can represent the expression for frequency-modulated wave by using a sine or cosine work for the vitality of the baseband signal. <br>We know wave equation as: </p>',unsafe_allow_html=True)

    st.latex(r'''
        m(t) = A_m cos(\omega_m t + \Theta)
        
        ''')
    
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li>m(t) is the Balancing Signal,</li>\
                <li>A<sub>m</sub> is the Amplitude of Balancing Signal,</li>\
                <li>ω<sub>m</sub> is the Angular Recurrence of Tweaking Signal,</li>\
                <li>Θ is the Period of the Balancing Signal.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.write('<p class="my-custom-sub-text">when we try to modulate an input signal, we need an expression for carrier wave also </p>',unsafe_allow_html=True)

    st.latex(r'''
        C(t) = A_c cos(\omega_c t + \Theta)

        ''')
    
    st.write('<p class="my-custom-sub-text">From amplitude modulation, we need two sine or cosine waves for modulation </p>',unsafe_allow_html=True)

    st.latex(r'''
        m(t) = A_m cos(\omega_m t)

        ''')
    
    st.write('<p class="my-custom-sub-text">and</p>',unsafe_allow_html=True)
    
    st.latex(r'''
        c(t) = A_c cos(\omega_c t)

        ''')
    
    st.write('<p class="my-custom-sub-text">or</p>',unsafe_allow_html=True)

    st.latex(r'''
        m(t) = A_m cos(2\Pi f_m t)

        ''')
    
    st.write('<p class="my-custom-sub-text">and</p>',unsafe_allow_html=True)

    st.latex(r'''
        c(t) = A_c cos(2\Pi f_c t)

        ''')
    
    st.write('<p class="my-custom-sub-text">Then frequency modulated wave will be:</p>',unsafe_allow_html=True)

    st.latex(r'''
        f_m(t) = f_c + kAcos(2\Pi f_mt)

        ''')
    
    st.latex(r'''
        f_m(t) = f_c + km(t)

        ''')
    
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li>f<sub>m</sub>(t) is the Frequency Modulated Wave,</li>\
                <li>f<sub>m</sub> is the Frequency of Carrier Wave,</li>\
                <li>m(t) is the Modulating Signal,</li>\
                <li>k is the Proportionality Constant.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">2.4 Advantages of Frequency Modulation </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Some of the advantages of Frequency modulation are listed below:</p>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text">\
                <li>The Amplitude of FM wave remains constant over time. This helps in removing noise from received signal. </li>\
                <li>FM is resistant to single strength variation. </li>\
                <li>It enhances more efficient use of bandwidth. </li>\
                <li>FM is used in radio broadcasting because FM is known for its superior quality compared to other methods of modulation. </li>\
                <li>It improves and increase the capacity for communication. </li>\
                </ul>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">2.5 Disadvantage of Frequency Modulation </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Some of disadvantages of Frequency Modulation are listed below:</p>',unsafe_allow_html=True)

    
    st.markdown('<ul class="my-custom-sub-text">\
                <li>Modulation of wave increases the complexity in implementation. </li>\
                <li>It requires specialized equipment and knowledge to implement, which makes it less accessible. </li>\
                <li>Sometimes modulation leads to loss in quality of signal received, which reduces the clarity of transmitted data. </li>\
                <li>FM has a large bandwidth which makes it costlier. </li>\
                </ul>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">2.6 Application of Frequency Modulation </div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Frequency Modulation has many applications in science and technological field. Some of its real-life uses are mentioned below:</p>',unsafe_allow_html=True)

    
    st.markdown('<ul class="my-custom-sub-text">\
                <li>FM is used in radio broadcasting. </li>\
                <li>It is used by many radio stations to broadcast music over the radio (One must have heard the term FM in radio while listening it). </li>\
                <li>FM is used in radar. </li>\
                <li>It is used in seismic prospecting. </li>\
                <li>It is used in Electroencephalogram (EEG), which is a test of brain activity. </li>\
                <li>Frequency modulation is superior to other modulations. That\'s why it has many applications in various fields. </li>\
                </ul>',unsafe_allow_html=True)
    



    #----------------------Phase Modulation-------------------------#
    st.markdown('<div class="my-custom-h5-text">3. Phase Modulation (PM)</div>',unsafe_allow_html=True)

    image_path5 = 'modulation/images/phase_signal.png'  # Replace with your image path
    image = Image.open(image_path5)

    st.write('<p class="my-custom-sub-text">Phase modulation (PM) is a kind of signal modulation in which the phase of a high-frequency \
             signal or carrier wave is made to change with its amplitude in proportion to the amplitude of the input signal. \
             This technique modulates information by changing the phase angle of the carrier signal, not its amplitude like the former techniques. \
             PM is very common in radio and television transmissions and in modem digital data transmission because of its capability \
             to operate efficiently in a noisy environment. Phase modulation therefore works as follows: \
             depending on the input signal, the carrier’s phase is shifted to encode and transmit information over different channels. </p>\
            <figure style="text-align: center;">\
            <img src="data:image/png;base64,{}" alt="Centered Image"><br>\
            <figcaption style="font-size:18px;font-weight:bold;font-family: Georgia, serif;">Fig. 5 Representation of Phase Modulation Signal</figcaption>\
            </figure><br>\
             '.format(image_to_base64(image_path5)),unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">The equation of a PM signal is represented by: </p>',unsafe_allow_html=True)

    st.latex(r'''
        V(t) = A cos[\omega_c t+ \Phi(t)]
        
        ''')
    
   
    st.markdown(
                '<p class="my-custom-sub-text">Where, <br> \
                <ul class="my-custom-sub-text" style="margin-left:20px;">\
                <li>ω<sub>c</sub> is the carrier frequency constant,</li>\
                <li>A is the amplitude constant,</li>\
                <li>Φ(t) is the phase angle, which is not constant. It is a function of the baseband signal.</li>\
                </ul>\
                </p>', unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">3.1 Advantages of Phase Modulation</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Some of the advantages of Frequency modulation are listed below:</p>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text">\
                <li><b>Fast:</b> Stage tweak is considered one of the quickest balance methods. It is because of the beat age at high velocity.</li>\
                <li><b>Low Sign power Utilization:</b> PM requires low sign power utilization because of its improved proficiency and quick speed.</li>\
                <li><b>Basic Circuit Plan:</b> The parts expected in the stage-tuned circuit are less when contrasted with FM. Subsequently, it has a basic circuit plan.</li>\
                </ul>',unsafe_allow_html=True)
    
    st.markdown('<div class="my-custom-h5-text">3.2 Disadvantages of Phase Modulation</div>',unsafe_allow_html=True)

    st.write('<p class="my-custom-sub-text">Some of disadvantages of Frequency Modulation are listed below:</p>',unsafe_allow_html=True)

    st.markdown('<ul class="my-custom-sub-text">\
                <li><b>Lower resistance:</b> PM has less resistance than FM. It is on the grounds that the frequencies are less impacted by outer aggravations than stage. Subsequently, PM has a lower clamor insusceptibility than FM.</li>\
                <li><b>Complex hardware during transformation from FM to PM:</b> The transformation interaction from recurrence adjustment to stage tweak is intricate. It is because of the extra parts expected for the transformation.</li>\
                <li><b>Susceptibility to Noise:</b> PM signals are more susceptible to noise and interference, especially phase noise, which can distort the signal. </li>\
                </ul>',unsafe_allow_html=True)


    
