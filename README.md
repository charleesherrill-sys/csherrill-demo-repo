# Notional SaaS License Manager

A tiny, notional Python app for demoing Devin Desktop, CLI, and DeepWiki.

It models a simple SaaS license manager where products have a fixed seat count and customers can provision or deprovision seats. There is a deliberate bug in the seat-provisioning logic that a failing test exposes.

## Run the tests

```bash
python -m pytest
```

## Files

- `license_manager.py` — core logic and in-memory store
- `tests/test_licenses.py` — pytest suite
- `pyproject.toml` — minimal project config

## The bug

`license_manager.py` rejects a request when `used_seats + requested_seats == total_seats`. It should only reject when `used_seats + requested_seats > total_seats`. This means a customer cannot use their last available seat.
