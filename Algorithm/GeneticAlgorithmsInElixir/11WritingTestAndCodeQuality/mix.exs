defmodule Mix.Tasks.Compile.Nif do
  use Mix.Task.Compiler

  def run(_args) do
    {result, _errcode} =
      System.cmd(
        "gcc",
        ["-fpic", "-shared", "-o", "genetic.so", "src/genetic.c"],
        stderr_to_stdout: true
      )

    IO.puts(result)
  end
end

defmodule Genetic.MixProject do
  use Mix.Project

  def project do
    [
      app: :genetic,
      version: "0.1.0",
      elixir: "~> 1.9",
      start_permanent: Mix.env() == :prod,
      compilers: [:nif] ++ Mix.compilers(),
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger],
      mod: {Genetic.Application, []}
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      {:libgraph, "~> 0.13"},
      {:gnuplot, "~> 1.19"},
      # {:alex, "~> 0.3.2"},
      {:benchee, "~> 1.0.1"},
      {:credo, "~> 1.4", only: [:dev, :test], runtime: false},
      {:stream_data, "~> 0.5", only: :test},
      {:dialyxir, "~> 1.0", only: [:dev], runtime: false}
    ]
  end
end
