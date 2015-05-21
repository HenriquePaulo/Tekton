var produtoModulo =angular.module('produtoModulo',[]);

produtoModulo.directive('produtoform', function(){
    return{
      restrict:'E',
      replace:true,
      template:'<input type="text" />'

    };
});

