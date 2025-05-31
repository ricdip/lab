{
  description = "algorithms lab";
  inputs = {
    utils.url = "github:numtide/flake-utils";
  };
  outputs =
    {
      self,
      nixpkgs,
      utils,
    }:
    utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShell = pkgs.mkShell {
          packages = with pkgs; [
            python310
            poetry
          ];
          shellHook = ''
            echo "This project uses python-poetry. Type 'poetry run jupyter notebook' to open web interface."
          '';
          env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc.lib
            pkgs.libz
          ];
        };
      }
    );
}
