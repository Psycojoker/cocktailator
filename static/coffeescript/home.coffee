IngredientsView = Backbone.View.extend
    el: $("#base")
    events:
        "click #ingredients input": "get_cocktails"
        "input #filtering input": "filter_ingredients"

    initialize: ->
        console.log "Ingredients view"
        console.log @el
        @render_ingredients()
        $("#cocktails").html("<p>Selectionne des ingrédients dans la colonne de gauche</p>")

    render_ingredients: ->
        that = this
        $.get "/ingredients/",
            (content) ->
                that.$el.find("#ingredients").html("<form>#{content}</form>")

    get_cocktails: ->
        that = this
        $.get "/cocktails/",
            that.$el.find("form").serialize(),
            (content) ->
                that.$el.find("#cocktails").html(content)

    filter_ingredients: ->
        that = this
        if that.$el.find("#filtering").find("input").val()
            $.get "/ingredients/",
                filtering_string: that.$el.find("#filtering").find("input").val()
                (content) ->
                    that.$el.find("#ingredients").html("<form>#{content}</form>")
        else
            @render_ingredients()


ingredients_view = new IngredientsView()
