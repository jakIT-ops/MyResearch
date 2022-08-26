defmodule DummyProblem do
  @behaviour Problem
  alias Types.Chromosome

  @impl true
  def genotype do
    genes = for _ <- 1..100, do: Enum.random(0..1)
    %Chromosome{genes: genes, size: 100}
  end

  @impl true
  def fitness_function(chromosome), do: Enum.sum(chromosome.genes)

  @impl true
  def terminate?(_population, generation), do: generation == 1
end

Genetic.run(DummyProblem)
