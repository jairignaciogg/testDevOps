public with sharing class ClasePrueba1 {
    public static void ClasePrueba1() {
        System.debug('Entra');
        List<Account> lsAcc = new List<Account>();
        lsAcc = [SELECT Id FROM Account LIMIT 200];
    }
}
