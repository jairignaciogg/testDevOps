public with sharing class ClasePrueba1 {
    public static void ClasePrueba1() {
        List<Account> lsAcc = new List<Account>();
        lsAcc = [SELECT Id FROM Account LIMIT 200];
        System.debug('Debug 1 a1');
    }
}