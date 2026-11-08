# Validation plan

## Required checks

- [ ] Count all audio files; compare with the reported 94 tracks.
- [ ] Verify every WAV can be decoded; report sample rate, channels, duration, bit depth/subtype.
- [ ] Check whether every track is 48,000 Hz; do not silently resample.
- [ ] Match filenames and metadata rows using explicit identifiers or normalized stems; manually review ambiguous matches.
- [ ] Detect missing rows, duplicate filenames, duplicate identifiers and duplicate content hashes.
- [ ] Review metadata field names, missing values, duration discrepancies, and claimed tempo/key/genre labels.
- [ ] Verify that audio is synthetically produced and describe the actual production workflow.
- [ ] Verify composition, recording, vocal, performance, sample and other third-party rights where applicable.
- [ ] Decide licensing only after the rights review.
- [ ] Create a frozen manifest, validation report and dataset card for the release version.

## Audit policy

The supplied audit script is **read-only with respect to the dataset**. It produces JSON/CSV reports in a separate report directory. It does not fix metadata, rename files, or modify audio automatically. All proposed corrections require review against source material.

## Important limitations

Technical metadata checks do not establish that BPM, key, genre, mood or other semantic annotations are correct. Those require separate evaluation, including manual listening and/or reproducible algorithms. A clean report is not proof of originality or rights clearance.
