public with sharing class ClasePrueba3 {
    public static void metodo() {
        List<Account> lsAcc = new List<Account>();
        lsAcc = [SELECT Id FROM Account LIMIT 200];
        System.debug('Debug 113');
    }
}