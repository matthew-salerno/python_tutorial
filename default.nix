{ pkgs ? import <nixpkgs> { } }:
# You don't need to worry about this package, it is for myBinder setup
# (unless you like nix package manager but that's a different rabbit hole)
pkgs.mkShell {
  buildInputs = [
     pkgs.python3Packages.matplotlib
     pkgs.python3Packages.ipywidgets
     pkgs.python3Packages.jupyterlab
  ];
}