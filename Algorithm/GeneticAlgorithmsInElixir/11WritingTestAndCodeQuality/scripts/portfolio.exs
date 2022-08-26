defmodule Portfolio do
  @behaviour Problem
  alias Types.Chromosome

  @impl true
  def genotype do
    genes = for _ <- 1..100, do: {:rand.uniform(10), :rand.uniform(10)}
    %Chromosome{genes: genes, size: 100}
  end

  @impl true
  def fitness_function(chromosome) do
    chromosome
    |> Enum.map(fn {roi, risk} -> 2 * roi - risk end)
    |> Enum.sum()
  end

  @impl true
  def terminate?(population, _generation), do: Enum.max_by(population, &Portfolio.fitness_function/1) == 20
end
