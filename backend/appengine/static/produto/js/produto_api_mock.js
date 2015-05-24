/**
 * Created by paulo on 24/05/15.
 */
var rest = angular.module('rest',[]);
        rest.factory('ProdutoApi',function($rootScope){
           return{
               salvar:function(produto){
                   var obj={};
                   obj.success = function(fcnSucesso){
                       obj.fcnSucesso = fcnSucesso;
                   };
                   obj.error = function(fcnErro){
                       obj.fcnError = fcnErro;
                   };
                   setTimeout(function(){
                    produto.id=1;
                    obj.fcnSucesso(produto)
                       $rootScope.$digest();
                   },1000);
                   return obj;
               }
           };
        });