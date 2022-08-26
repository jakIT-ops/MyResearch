defmodule TigerSimulation do
  @behaviour Problem
  alias Types.Chromosome

  @impl true
  def genotype do
    genes = for _ <- 1..8, do: Enum.random(0..1)
    %Chromosome{genes: genes, size: 8}
  end

  @impl true
  def fitness_function(chromosome) do
    tropic_scores = [0.0, 3.0, 2.0, 1.0, 0.5, 1.0, -1.0, 0.0]
    tundra_scores = [1.0, 3.0, -2.0, -1.0, 0.5, 2.0, 1.0, 0.0]
    traits = chromosome.genes

    traits
    |> Enum.zip(tundra_scores)
    |> Enum.map(fn {t, s} -> t*s end)
    |> Enum.sum()
  end

  @impl true
  def terminate?(_population, generation), do: generation == 150

  def average_tiger(population) do
    genes = Enum.map(population, & &1.genes)
    fitnesses = Enum.map(population, & &1.fitness)
    ages = Enum.map(population, & &1.age)
    num_tigers = length(population)

    avg_fitness = Enum.sum(fitnesses) / num_tigers
    avg_age = Enum.sum(ages) / num_tigers
    avg_genes =
      genes
      |> Enum.zip()
      |> Enum.map(& Enum.sum(Tuple.to_list(&1)) / num_tigers)

    %Chromosome{genes: avg_genes, age: avg_age, fitness: avg_fitness}
  end
end

import Gnuplot

tiger = Genetic.run(TigerSimulation,
                    population_size: 5,
                    selection_rate: 0.9,
                    mutation_rate: 0.1)

IO.write("\n")

stats =
  :ets.tab2list(:statistics)
  |> Enum.map(fn {gen, stats} -> [gen, stats.mean_fitness] end)

{:ok, cmd} =
  plot([
    [:set, :title, "mean fitness versus generation"],
    [:plot, "-", :with, :points]
    ], [stats])

# {_, zero_gen_stats} = Utilities.Statistics.lookup(0)
# {_, fivehundred_gen_stats} = Utilities.Statistics.lookup(500)
# {_, onethousand_gen_stats} = Utilities.Statistics.lookup(1000)

# IO.inspect(zero_gen_stats.average_tiger)
# IO.inspect(fivehundred_gen_stats.average_tiger)
# IO.inspect(onethousand_gen_stats.average_tiger)
