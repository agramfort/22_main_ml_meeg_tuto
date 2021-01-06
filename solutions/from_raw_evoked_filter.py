raw_fname = data_path + '/MEG/sample/sample_audvis_raw.fif'
raw = mne.io.read_raw_fif(raw_fname)
# get events with find_events
events = mne.find_events(raw)
# define event_id
event_id = {'auditory/left': 1}
# define tmin, tmax, reject
tmin, tmax = -0.2, 0.5
reject = {'eog': 150e-6}
# define baseline or highpass filter data at 1Hz
baseline = (None, 0)
# define picks
picks = mne.pick_types(raw.info, meg='mag', eog=True)
# construct epochs
epochs = mne.Epochs(raw, events, event_id, tmin=tmin, tmax=tmax,
                    reject=reject, picks=picks, baseline=baseline)
# average and plot the evoked
evoked = epochs.average()
evoked.plot()
