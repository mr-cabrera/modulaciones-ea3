#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FSK_simulacion
# Author: Matias Gandino
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class FSK_simulacion(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FSK_simulacion", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FSK_simulacion")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "FSK_simulacion")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.frecuencia_1 = frecuencia_1 = 1000
        self.frecuencia_0 = frecuencia_0 = 3000
        self.samp_rate = samp_rate = 32000
        self.low_cutoff_1 = low_cutoff_1 = frecuencia_1-200
        self.low_cutoff_0 = low_cutoff_0 = frecuencia_0-200
        self.interpolation = interpolation = 100
        self.high_cutoff_1 = high_cutoff_1 = frecuencia_1+200
        self.high_cutoff_0 = high_cutoff_0 = frecuencia_0+200

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_sink_x_1_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Pulsos", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_sink_x_1_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_1_0_0_win)
        self.qtgui_sink_x_1_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Salida Demodulada", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_1_0_win = sip.wrapinstance(self.qtgui_sink_x_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_1_0_win)
        self.qtgui_sink_x_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Salida Demodulada", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((0, 0, 0, 1, 1, 1, 0, 1), True, 1, )
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, interpolation)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(100, 0.01, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(100, 0.01, 4000, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-1))
        self.band_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                low_cutoff_0,
                high_cutoff_0,
                1,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                low_cutoff_1,
                high_cutoff_1,
                1,
                window.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frecuencia_0, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frecuencia_1, 1, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, (-1))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_repeat_0, 0), (self.qtgui_sink_x_1_0_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_sink_x_1_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_uchar_to_float_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "FSK_simulacion")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_frecuencia_1(self):
        return self.frecuencia_1

    def set_frecuencia_1(self, frecuencia_1):
        self.frecuencia_1 = frecuencia_1
        self.set_high_cutoff_1(self.frecuencia_1+200)
        self.set_low_cutoff_1(self.frecuencia_1-200)
        self.analog_sig_source_x_0.set_frequency(self.frecuencia_1)

    def get_frecuencia_0(self):
        return self.frecuencia_0

    def set_frecuencia_0(self, frecuencia_0):
        self.frecuencia_0 = frecuencia_0
        self.set_high_cutoff_0(self.frecuencia_0+200)
        self.set_low_cutoff_0(self.frecuencia_0-200)
        self.analog_sig_source_x_0_0.set_frequency(self.frecuencia_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_cutoff_1, self.high_cutoff_1, 1, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_1.set_taps(firdes.band_pass(1, self.samp_rate, self.low_cutoff_0, self.high_cutoff_0, 1, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_1_0_0.set_frequency_range(0, self.samp_rate)

    def get_low_cutoff_1(self):
        return self.low_cutoff_1

    def set_low_cutoff_1(self, low_cutoff_1):
        self.low_cutoff_1 = low_cutoff_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_cutoff_1, self.high_cutoff_1, 1, window.WIN_HAMMING, 6.76))

    def get_low_cutoff_0(self):
        return self.low_cutoff_0

    def set_low_cutoff_0(self, low_cutoff_0):
        self.low_cutoff_0 = low_cutoff_0
        self.band_pass_filter_1.set_taps(firdes.band_pass(1, self.samp_rate, self.low_cutoff_0, self.high_cutoff_0, 1, window.WIN_HAMMING, 6.76))

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation
        self.blocks_repeat_0.set_interpolation(self.interpolation)

    def get_high_cutoff_1(self):
        return self.high_cutoff_1

    def set_high_cutoff_1(self, high_cutoff_1):
        self.high_cutoff_1 = high_cutoff_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_cutoff_1, self.high_cutoff_1, 1, window.WIN_HAMMING, 6.76))

    def get_high_cutoff_0(self):
        return self.high_cutoff_0

    def set_high_cutoff_0(self, high_cutoff_0):
        self.high_cutoff_0 = high_cutoff_0
        self.band_pass_filter_1.set_taps(firdes.band_pass(1, self.samp_rate, self.low_cutoff_0, self.high_cutoff_0, 1, window.WIN_HAMMING, 6.76))




def main(top_block_cls=FSK_simulacion, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
