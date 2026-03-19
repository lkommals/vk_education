package ru.vk.education.job;

import java.util.List;

public class Job {
    private final String name;
    private final String company;
    private final List<Skill> tags;
    private final int experience;

    public Job(String name, String company, List<Skill> tags, int experience) {
        this.name = name;
        this.company = company;
        this.tags = tags;
        this.experience = experience;
    }

    public String getName() {
        return name;
    }

    public String getCompany() {
        return company;
    }

    public List<Skill> getTags() {
        return tags;
    }

    public int getExperience() {
        return experience;
    }

    @Override
    public String toString() {
        return name + " at " + company;
    }
}