public class DessertProcedures {
    private static String measureIngredient(String ingredient, int cups) {
        return "Measure " + cups + " cups of " + ingredient + ".";
    }
    private static String mixDessertBatter(String ingredient) {
        return "Mix " + ingredient + " with sugar, eggs, and milk.";
    }
    private static String bakeDessert(int temperatureF, int minutes) {
        return "Bake at " + temperatureF + " F for " + minutes + " minutes.";
    }
    public static String[] prepareDessert(String ingredient, int cups, int temperatureF, int minutes) {
        return new String[] {measureIngredient(ingredient, cups),
            mixDessertBatter(ingredient), bakeDessert(temperatureF, minutes)};
    }
    public static void main(String[] args) {
        for (String step : prepareDessert("flour", 2, 350, 25)) {
            System.out.println(step);
        }
        System.out.println("Changed arguments:");
        for (String step : prepareDessert("oat flour", 3, 325, 30)) {
            System.out.println(step);
        }
    }
}
