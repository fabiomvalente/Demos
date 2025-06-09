package com.aulaSpring.webservice.resources;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aulaSpring.webservice.entities.Category;
import com.aulaSpring.webservice.services.CategoryService;

@RestController
@RequestMapping(value ="/categories")
public class CategoryResource {
    
    @Autowired
    private CategoryService service;

    @GetMapping
    public ResponseEntity<List<Category>> findAll() {
        List<Category> Category = service.findAll();
        return ResponseEntity.ok().body(Category);
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Category> findById(@PathVariable Long id) {
        Category Category = service.findById(id);
        return ResponseEntity.ok().body(Category);
    }
    
}
