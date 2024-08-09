# Noisy voter model with restricted interactions

Python implementation of noisy voter model via Gillespie method with added restrictions. In this model some vertices are omitted from the network of opinions (see graph reference below), meaning certain opinions can't interact directly. Here we only analyse cases with 3 and 4 opinions.
<div align="center">
  <img alt="graphs used in simulation" src="figs/graph_reference.png"/>
</div>

## Requirements

- numpy (tested with 2.0.0)
- typer (tested with 0.12.3)
- typing_extensions (tested with 4.12.2)

## Usage of Gillespie method
none

## Acknowledgements

This code was written as a part of summer internship project "Influence of the state interaction network on the statistical properties of the voter model". Internship was supported by [Research Council of Lithuania](https://lmt.lrv.lt) (P-SV-24-28). Internship was supervised by [Aleksejus Kononovicius](https://kononovicius.lt).
