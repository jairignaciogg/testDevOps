public with sharing class ClasePrueba2 {
    public static void ClasePrueba2() {
        List<Account> lsAcc = new List<Account>();
        lsAcc = [SELECT Id FROM Account LIMIT 200];
        System.debug('Debug 2 hola');
    }
}