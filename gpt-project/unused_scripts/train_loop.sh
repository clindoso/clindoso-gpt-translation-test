#!/bin/bash
while true; do
  python train_robbert.py
  echo "Training crashed with exit code $?.  Respawning.." >&2
  sleep 1
done
