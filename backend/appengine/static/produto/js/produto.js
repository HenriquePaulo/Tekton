var produtoModulo =angular.module('produtoModulo',['rest']);

produtoModulo.directive('produtoform', function(){
    return{
      restrict:'E',
      replace:true,
      templateUrl:'/static/produto/js/produto_form.html',
      scope:{
          product: '='
      },
     controller:function($scope,ProdutoApi){
         $scope.salvandoFlag=false;
         $scope.salvar = function(){
             $scope.salvandoFlag=true;
             $scope.errors={};
             var promessa = ProdutoApi.salvar($scope.product);
             promessa.success(function(product){
                 console.log(product);
                 $scope.product.nome='';
                 $scope.product.titulo='';
                 $scope.product.descricao='';
                 $scope.product.imagem='';
                 $scope.product.preco='';
                 $scope.salvandoFlag=false;
             })
             promessa.error(function(errors){
                 $scope.errors=errors;
                 console.log(errors);
                 $scope.salvandoFlag=false;

             })

         }
     }

    };
});

produtoModulo.directive('produtolinha', function(){
    return{

      replace:true,
      templateUrl:'/static/produto/js/produto_linha_tabela.html',
      scope:{
          product: '='
      },
     controller:function($scope,ProdutoApi){

     }

    };
});


