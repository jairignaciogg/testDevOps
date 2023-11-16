public with sharing class ClasePrueba1 {
    public static void metodo() {
        List<Account> lsAcc = new List<Account>();
        lsAcc = [SELECT Id FROM Account LIMIT 200];
        System.debug('Se modifica Clase');
    }
}